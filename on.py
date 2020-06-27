#!/usr/bin/python3

import time
import board
import neopixel
from random import random
from math import floor


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D21

# The number of NeoPixels
num_pixels = 999

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.6, auto_write=False, pixel_order=ORDER
)

def dec_rgb(n, px):
  rgb_minus = (n,)*3
  new_px = map(lambda a,b: max(0, min(a-b, 255)), px, rgb_minus)
  return tuple(new_px)



if __name__ == "__main__":
  pixels.fill((80, 70, 40))
  pixels.show()
