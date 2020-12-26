# Imports scraping methods
import scrapy
# Note that running CrawlerProcess hadndles the Twisted reactor for us rather
# than us run it manually--we want to use CrawlerRunner
from scrapy.crawler import CrawlerProcess
# Imports custom screen module from fellow module
import piOLED


# To integrate a crawler inside a larger script, include its class definition
# as well 'from scrapy.crawler import CrawlerProcess'
class CovidSpider(scrapy.Spider):
    # This name must uniquely identify a spider within a project
    name = 'covid_numbers'

    start_urls = ['https://www.worldometers.info/coronavirus/']

    # We can apply custom_srettings to be run by default by editing
    # the following dictionary:

    # custom_settings = {
    #     'DOWNLOAD_DELAY': 8,
    #     'CONCURRENT_REQUESTS': 1,
    #     'AUTOTHROTTLE_ENABLED': True,
    #     'AUTOTHROTTLE_START_DELAY': 5,
    #     }

    # parse() changed to reflect new format of worldometer.info's data
    def parse(self, response):
        # Obtain total number of cases in the world (dead/alive/current)
        #
        # Note that we use xpath in order to extract this
        total_cases = response.xpath(
            '//span[@style="color:#aaa"]/text()').extract_first()[:-1]

        yield {'total_cases': total_cases}


def storeData(filename):
    # Determines the output file for use with the rest of the script
    #
    # Note that additional settings (such as silencing the output of
    # logs for this particular spider) may be added by adding more
    # entries to the settings dictionary below (see the following:
    #
    # docs.scrapy.org/en/latest/topics/settings.html#topics-settings-ref
    process = CrawlerProcess(settings={"FEEDS": {
        filename: {"format": "csv"}}, "LOG_ENABLED": False})

    # Sets crawling using WeatherSpider
    process.crawl(CovidSpider)

    # Script stays at this step until crawling is finished
    process.start()

    with open(filename, 'r') as f:
        # Grabs the line pertaining to the temp, wind speed, and condition
        # specifically (definitely should clean up)
        rawData = f.read().split('\n')[1].split(',')

        covidData = {'cases': rawData[0]}

        return covidData


# Sends info to OLED display
def broadcast(screen):
    pass


def main():
    screen = piOLED.OLED()

    data = storeData()

    screen.align(data['cases'], 'center')

    piOLED.GPIO.cleanup()


if __name__ == '__main__':
    main()