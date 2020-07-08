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
num_pixels = 126

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
def scroll_array(pixels):
    move = 1
    ar = pixels[move::] + pixels[:move]
    for i, val in enumerate(ar):
        pixels[i] = val
    return pixels

def mirror_array(pivot, array):
    bottom = array[0:pivot+1]
    top = array[pivot::-1]
    full = bottom + top
    mirrored = copy.deepcopy(array)
    for i, val in enumerate(full[0:len(array)-1]):
        mirrored[i] = val
    return mirrored

# for array of single int values, map that onto the same position in pixels
# using equal RGB to the integer input
def map_to_pix(ar, pixels):
    for i in range(0, pixels.n):
      pixels[i] = (ar[i], ar[i], ar[i])
    return pixels

# top of the scrolling function
def scroll(fade, pixels):
    periodicity = 3
    SAMPLES = math.ceil(pixels.n / periodicity)
    SCALE = 0,255 ## Output range

    ## Angles in degrees for which to calculate sine
    angles = [ rescale(i,0,SAMPLES,180,360, ) for i in range(SAMPLES) ]
    sin_table = [ int(round(rescale(s,-1,1,SCALE[0],SCALE[1]))) for s in [
        math.sin(math.radians(a)) for a in angles ]]
    pixels = map_to_pix(sin_table * math.ceil(periodicity), pixels)
    pivot = math.floor( len(pixels)/2 )

    while True:
        pixels = scroll_array(pixels)
        mirror_pixels = mirror_array(pivot, pixels)
        mirror_pixels.show()
        time.sleep(fade)


if __name__ == "__main__":
    # use with so ctrl-c kills the lights when done.
    with neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER) as strip:
      scroll(0.03, strip)
