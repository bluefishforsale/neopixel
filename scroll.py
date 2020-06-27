#!/usr/bin/python3

import time
import board
import neopixel
from random import random
import math
from pprint import pprint

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D21

# The number of NeoPixels
num_pixels = 500

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB


## Generate sine table
def rescale(X,A,B,C,D,force_float=False):
    retval = ((float(X - A) / (B - A)) * (D - C)) + C
    if not force_float and all(map(lambda x: type(x) == int, [X,A,B,C,D])):
        return int(round(retval))
    return retval

# moves part of an array to the end or beginning based on direction
# preserves order of elements in the array
def scroll_array(move, ar):
    if move > 0:
        ar2 = ar[move::] + ar[:move]
    elif move < 0:
        ar2 = ar[-move:] + ar[:-move]
    for i, val in enumerate(ar2):
        pixels[i] = val
    return ar

# for array of single int values, map that onto the same position in pixels
# using equal RGB to the integer input
def map_to_pix(ar, pixles):
    for i in range(0, pixels.n):
      pixels[i] = (ar[i], ar[i], ar[i])
    return pixels

# top of the scrolling function
def scroll(fade):
    global pixels
    periodicity = 10
    SAMPLES = math.ceil(pixels.n / periodicity)
    SCALE = 0,255 ## Output range

    ## Angles in degrees for which to calculate sine
    angles = [ rescale(i,0,SAMPLES,90,360, ) for i in range(SAMPLES) ]
    sin_table = [ int(round(rescale(s,-1,1,SCALE[0],SCALE[1]))) for s in [
        math.sin(math.radians(a)) for a in angles ]]
    pixels = map_to_pix(sin_table * math.ceil(periodicity), pixels)
    while True:
        pixels = scroll_array(fade, pixels)
        pixels.show()


if __name__ == "__main__":
    # use with so ctrl-c kills the lights when done.
    with neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER) as pixels:
      scroll(1)
