# Author: Karandeep Singh Nagra

'''
An adaptation of Iwan Smith's simulate.m to Python.  Instead of piping the output of main.c into krackoutput,
send it to a file named out:
./main > out

Run this script in the same folder as the file out, and a window will pop up with an animation of the board.
'''

dataFile = open('out', 'r')

