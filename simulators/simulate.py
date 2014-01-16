# Author: Karandeep Singh Nagra
# NOTE: YOU NEED PYGAME AND NUMPY TO RUN THIS PROGRAM
'''
An adaptation of Iwan Smith's simulate.m to Python.  Instead of piping the output of main.c into krackoutput,
send it to a file named out:
./main > out

Run this script in the same folder as the file out, and a window will pop up with an animation of the board.
'''

import sys, pygame
from numpy import *
pygame.init()

dataFile = open('out', 'r')

RADIUS = 5  # radius of each pixel; this is used to define the entire board and calculate position of pixels, etc.

size = width, height = RADIUS * 2 * 48, RADIUS * 2 * 24

screen = pygame.display.set_mode(size)
frame = 0

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED =   (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE =  (  0,   0, 255)

red_data = zeros( (18, 64) )
green_data = zeros( (18, 64) )
blue_data = zeros( (18, 64) )

red_image = zeros( (24, 48) )
green_image = zeros( (24, 48) )
blue_image = zeros (24, 48) )

def pos(x):
  return (x * RADIUS * 2) + RADIUS

while 1:
  screen.fill(BLACK)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
    
  for panel in range(18):
    linedata = dataFile.readline()
    red_data[panel, : ] = linedata[3:66]
    green_data[panel, : ] = linedata[67:130]
    blue_data[panel, : ] = linedata[131:194]
    
  panel = 1
  for pan_hor in range(6):
    for pan_ver in range(3):
      panel = pan_hor + 1 + (pan_ver * 6)
      for line in range(8):
        red_image[pan_ver*8+line+1, range(pan_hor*8+1, pan_hor*8+8+1)] = red_data[panel, range(line*8+1, line*8+8+1)]
        green_image[pan_ver*8+line+1, range(pan_hor*8+1, pan_hor*8+8+1)] = green_data[panel, range(line*8+1, line*8+8+1)]
        blue_image[pan_ver*8+line+1, range(pan_hor*8+1, pan_hor*8+8+1)] = blue_data[panel, range(line*8+1, line*8+8+1)]
  
  for x in range(24):
    for y in range(48):
      pygame.draw.circle(screen, [pos(x), pos(y)], [red_image[x, y], green_image[x, y], blue_image[x, y], RADIUS)
    
  pygame.display.flip()
  frame = frame + 1
