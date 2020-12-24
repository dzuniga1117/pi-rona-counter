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
    def __init__():
        pass

    # Displays message at the given (x, y) coordinate in the display
    def write(message, x, y):
        pass

    # Aligns message along a specified place on the display
    def align(message, alignment=default):
        pass
