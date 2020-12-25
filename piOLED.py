# The purpose of this file is to create an easier-to-use set of functions
# that aim to simplify drawing text to an OLED display using the
# Adafruit_SSD1306 library and PIL Image modules--this will be used alongside
# the main counter module to write statistics to the display

# This allows us to interface with our OLED display
import Adafruit_SSD1306
# We need some additional modules in order to get pictures
# and text to be displayed on our OLED screen (Python Imaging
# Library)
from PIL import Image, ImageFont, ImageDraw
# The following allows us to manage GPIO pins for our Pi:
import RPi.GPIO as GPIO


class OLED():
    def __init__(self):
        # Initialize the display with the Adafruit module
        self.RST = 24
        self.disp = Adafruit_SSD1306.SSD1306_128_64(rst=self.RST)
        self.disp.begin()

        # Establish display dimensions
        self.width = self.disp.width
        self.height = self.disp.height

        # Clear screen contents upon initialization
        self.disp.clear()
        self.disp.display()

        # Create image buffer for use with the other class methods
        self.image = Image.new('1', (self.width, self.height))

        # Create the drawing object for the given OLED display
        self.draw = ImageDraw.Draw(self.image)

        # Establish font in order to show text on the display
        self.font = ImageFont.load_default()

    # Displays a default message in order to test class abilities
    def sampleText(self):
        self.draw.text((0, 0), 'Hello,\nRaspberry Pi!', font=self.font,
                       fill=255)

        # Update display
        self.disp.image(self.image)
        self.disp.display()

    # Displays message at the given (x, y) coordinate in the display
    def write(self, message, x, y):
        pass

    # Aligns message along a specified place on the display
    def align(self, message, alignment):
        pass


def main():
    screen = OLED()

    # Display sample text
    screen.sampleText()

    # Clear up pins after finishing script
    GPIO.cleanup()


if __name__ == '__main__':
    main()
