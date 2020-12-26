# pi-rona-counter
A simple COVID-19 case tracker that keeps track of the total number of cases since the outbreak (regardless of outcome) using an OLED display connected to a Raspberry Pi.

## Files
#### piOLED.py
- Contains a modified version of the **Adafruit_SSD1306 module** in order to simplify the process of writing information to the display. Contains a variety of alignment methods that make organization easier with 9 positions, with freeform text locations also possible.

#### covidCounter.py
- Contains the Scrapy web crawler responsible for obtaining the number of cases taken from worldometers.info/coronavirus and is also responsible for initializing the requests. This is the main portion of the script and is called upon by our shell script below.

#### covidLoop.sh
- Tells the system to run covidCounter.py every minute and update the contents of the screen. This is done as a quick and dirty workaround against the non-reusable nature of Scrapy spiders (at least without further work).

#### covid_numbers.csv
- Contains the actual data from which covidCounter.py reads/writes to on every call.

## How to Use
Using any standard 128x64 SSD1306 OLED display, connect your Pi of choice as follows:
1. Vcc to GPIO Pin 1
2. Gnd to GPIO Pin 14
3. SCL to GPIO Pin 5
4. SDA to GPIO Pin 3

Once that is complete, ensure that the Adafruit_SSD1306 (mind the spelling) module is installed on your system (note to reader: this module has apparently been deprecated recently, may update project later to use a more modern one). Users must also make sure that the Scrapy module is also installed in order to get the tracker to update the number of cases. At this point, one is free to clone the repository to the Pi and navigate to the cloned directory. Run the program in the background by running

`./covidLoop.sh &`

The Pi will now update the total number of cases being tracked and update this number every minute (as well as tell the time below).
