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
        self.font = ImageFont.truetype("NotoSans-Regular.ttf", 12)

    # The following methods are utility methods that ensure that items are
    # displayed smoothly and are updated properly on the OLED display

    # Manually clears the screen from anything currently displaying on it by
    # drawing a blank rectangle (requires update(), used for smooth animations)
    def blankScreen(self):
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)

    # Updates the screen's contents (must be called in order to write changes
    # to the OLED display--none of the other drawing methods update the screen
    # unless update() is called)
    def update(self):
        self.disp.image(self.image)
        self.disp.display()

    # Displays a default message in order to test class abilities at (0, 0)
    def sampleText(self):
        self.draw.text((0, 0), 'Hello,\nRaspberry Pi!', font=self.font,
                       fill=255)

    # Note that the following drawing methods require update() call some point
    # in order to get the OLED display to reflect the changes in the buffer
    # introduced by these methods on the self.image object

    # Displays a message at the given (x, y) coordinate in the display
    def write(self, message, x, y):
        # Write to display
        self.draw.text((x, y), message, font=self.font, fill=255)

    # Aligns message along a specified place on the display by specifying one
    # of nine locations on the screen (default behavior is centered)
    def align(self, message, alignment='center'):
        # Obtain dimensions of message in terms of pixels, to keep in line with
        # pixel-centric needs of draw() functions
        msgPxWidth = len(message) * 6
        msgPxHeight = 11               # Accounts for chars like 'p', 'g', etc.

        # In order for alignment to work, we must consider size of pixels, not
        # just character sizes (using the default font, the width of a
        # character is 6 *pixels*, so we make the offset multiply by 6)
        #
        # Center alignment
        if alignment is 'center':
            self.draw.text((self.width / 2 - msgPxWidth / 2,
                           self.height / 2 - msgPxHeight / 2), message,
                           font=self.font, fill=255)
        # Top-center (title)
        if alignment is 'top_center':
            self.draw.text((self.width / 2 - msgPxWidth / 2, 0), message,
                           font=self.font, fill=255)
        # Top-left
        elif alignment is 'top_left':
            self.draw.text((0, 0), message, font=self.font, fill=255)
        # Top-right
        elif alignment is 'top_right':
            self.draw.text((self.width - msgPxWidth, 0), message,
                           font=self.font, fill=255)
        # Bottom-center
        if alignment is 'bottom_center':
            self.draw.text((self.width / 2 - msgPxWidth / 2,
                           self.height - msgPxHeight), message,
                           font=self.font, fill=255)
        # Bottom-left
        elif alignment is 'bottom_left':
            self.draw.text((0, self.height - msgPxHeight), message,
                           font=self.font, fill=255)
        # Bottom-right
        elif alignment is 'bottom_right':
            self.draw.text((self.width - msgPxWidth,
                           self.height - msgPxHeight), message,
                           font=self.font, fill=255)
        # Middle-left
        elif alignment is 'middle_left':
            self.draw.text((0, self.height / 2 - msgPxHeight / 2), message,
                           font=self.font, fill=255)
        # Middle-right
        elif alignment is 'middle_right':
            self.draw.text((self.width - msgPxWidth,
                           self.height / 2 - msgPxHeight / 2), message,
                           font=self.font, fill=255)


def main():
    # Initialize OLED object, 'screen'
    screen = OLED()

    # Demonstrates scrolling text
    # for i in range(0, 40, 2):
    #    screen.blankScreen()
    #    screen.write('ravioli', i, 0)
    #    screen.update()

    # Demonstrates alignment function at different corners of the display
    #
    # locations = ['top_left', 'top_center', 'top_right', 'middle_left',
    #              'center', 'middle_right', 'bottom_left', 'bottom_center',
    #              'bottom_right']
    #
    # for i in locations:
    #     screen.align('_X_', i)
    #     screen.update()

    screen.align('Title Text', 'top_center')
    screen.align('<<', 'middle_left')
    screen.align('>>', 'middle_right')
    screen.align('Menu', 'bottom_left')
    screen.align('Options', 'bottom_right')
    screen.update()

    # Clear up pins after finishing script
    GPIO.cleanup()


if __name__ == '__main__':
    main()
