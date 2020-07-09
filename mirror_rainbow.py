#!/usr/bin/python3

import time
import board
import neopixel
import copy
from random import random
import math
from pprint import pprint

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D21

# The number of NeoPixels
num_pixels = 290

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

def mirror_array(pivot, array):
    bottom = array[0:pivot]
    top = array[pivot::-1]
    full = bottom + top
    mirrored = copy.deepcopy(array)
    for i, val in enumerate(full[0:len(array)-1]):
        mirrored[i] = val
    return mirrored

def rainbow_cycle(wait):
    pivot = math.floor( len(pixels)/2  )
    while True:
        for j in range(255):
            for i in range(num_pixels):
                pixel_index = (i * 256 // num_pixels) + j
                pixels[i] = wheel(pixel_index & 255)
            mirror_pixels = mirror_array(pivot, pixels)
            mirror_pixels.show()
            time.sleep(wait)

if __name__ == "__main__":
    # use with so ctrl-c kills the lights when done.
    with neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER) as pixels:
      rainbow_cycle(0.000)
