# Author: Karandeep Singh Nagra
# NOTE: YOU NEED PYGAME AND NUMPY TO RUN THIS PROGRAM
'''
An adaptation of Iwan Smith's simulate.m to Python.  Instead of piping the output of main.c into krackoutput,
send it to a file named out:
gcc main.c <pixel_color_implementation.c>
./a.out > out

Run this script in the same folder as the file out, and a window will pop up with an animation of the board.

You can supply a delay between each frame in float seconds.  Otherwise, there is no delay, and the board is updated
as fast as PyGame can update it.

You can also supply a board-pixel radius in integer screen-pixels.
'''

import sys, pygame, time
from numpy import *
pygame.init()

if len(sys.argv) < 2:
  delay = 0
  RADIUS = 5  # radius of each pixel; this is used to define the entire board and calculate position of pixels, etc.
elif len(sys.argv) == 2:
  delay = float(sys.argv[1])
  RADIUS = 5
else:
  delay = float(sys.argv[1])
  RADIUS = int(sys.argv[2])

dataFile = open('out', 'r')

size = width, height = RADIUS * 2 * 48, RADIUS * 2 * 24

screen = pygame.display.set_mode(size) # the window that will pop up
board = pygame.Surface(size)  # a surface that covers the entire window; needed separate to rotate to correct orientation
frame = 0

#       (RED, GRN, BLU)
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED =   (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE =  (  0,   0, 255)

# arrays to hold each panel's pixel color intensities
red_data = zeros( (18, 64) )
green_data = zeros( (18, 64) )
blue_data = zeros( (18, 64) )

# arrays to hold the board's color intensities
red_image = zeros( (24, 48) )
green_image = zeros( (24, 48) )
blue_image = zeros( (24, 48) )

# return position in regard to RADIUS
# Maps: x in 24 or 48 -> pos(x) in height or width (declared above)
def pos(x):
  return (x * RADIUS * 2) + RADIUS
  
# return true color by scaling to 266 full values from 16
def true_color(r, g, b):
  return (r * 16, g * 16, b * 16)

while 1:
  board.fill(BLACK)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
    
  for panel in range(18):
    linedata = dataFile.readline()
    # First two chars in each line represent the board number
    for char in range(64):
      # All values have to be converted to ints from hex.
      green_data[panel, char] = int(linedata[2+char], 16)   # Next 64 are green values
      red_data[panel, char] = int(linedata[66+char], 16)    # Next 64 are red values
      blue_data[panel, char] = int(linedata[130+char], 16)  # Next 64 are blue values
    
  panel = 0
  # Map panel values to full board array:
  for pan_hor in range(6):
    for pan_ver in range(3):
      panel = pan_hor + (pan_ver * 6)
      for line in range(8):
        red_image[pan_ver*8+line, range(pan_hor*8, pan_hor*8+8)] = red_data[panel, range(line*8, line*8+8)]
        green_image[pan_ver*8+line, range(pan_hor*8, pan_hor*8+8)] = green_data[panel, range(line*8, line*8+8)]
        blue_image[pan_ver*8+line, range(pan_hor*8, pan_hor*8+8)] = blue_data[panel, range(line*8, line*8+8)]
  
  # Draw each pixel on the board Surface.
  for x in range(24):
    for y in range(48):
      pygame.draw.circle(board, true_color(red_image[x, y], green_image[x, y], blue_image[x, y]), [pos(y), pos(x)], RADIUS)
    
  board = pygame.transform.rotate(board, 180)
  screen.blit(board, [0, 0])
  pygame.display.flip()
  frame = frame + 1
  time.sleep(delay)
