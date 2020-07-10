#!/usr/bin/python3

import time
import board
import neopixel
import adafruit_fancyled.adafruit_fancyled as fancy
from random import random
from math import floor
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--hue',        default=255, type=int, help='what shade you be?')
parser.add_argument('-s', '--saturation', default=255, type=int, help='how deep is your shade?')
parser.add_argument('-b', '--brightness', default=255, type=int, help='how bright you is?')
parser.add_argument('-n', '--num_pixels', default=100, type=int,   help='how many led you got?')
args = parser.parse_args()

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D21

# The number of NeoPixels
num_pixels = args.num_pixels

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False, pixel_order=ORDER)

if __name__ == "__main__":
  rgbcolor = fancy.CHSV(args.hue, args.saturation, args.brightness)
  pixels.fill((255,255,255))
  pixels.show()
