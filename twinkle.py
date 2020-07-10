#!/usr/bin/python3

import time
import board
import neopixel
from random import random
from math import floor
from pprint import pprint
from concurrent.futures import ThreadPoolExecutor
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--brightness', default=0.5, type=float, help='how bright you is?')
parser.add_argument('-n', '--num_pixels', default=100, type=int, help='how many led you got?')
parser.add_argument('-s', '--speed',      default=1.05,   type=float, help='how fast it go?')
args = parser.parse_args()

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D21

# The number of NeoPixels
num_pixels = args.num_pixels

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

def dec_rgb(n, px):
  rgb_minus = (n,) * 3
  new_px = map(lambda a,b: max(0, min(floor(a / b), 255)), px, rgb_minus)
  return tuple(new_px)

def twinkle(fade):
  global pixels
  while True:
    # pick a pixel
    r = floor(( random() * 100000) % num_pixels)
    # set to max brightness
    pixels[r]=(255,255,255)

    with ThreadPoolExecutor(max_workers=8) as executor:
      for i in range(0, num_pixels):
          # fade all pixels down by X
          future = executor.submit(dec_rgb, fade, pixels[i] )
          pixels[i] = future.result()
    # print pixles to strip
    pixels.show()


if __name__ == "__main__":
    with neopixel.NeoPixel(pixel_pin, num_pixels, brightness=args.brightness, auto_write=False, pixel_order=ORDER) as pixels:
        twinkle(args.speed)
