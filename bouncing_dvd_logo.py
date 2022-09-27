"""Bouncing DVD Logo, by Al Sweigart al@inventwithpython.com
A bouncing DVD logo animation. You have to be "of a certain age" to
appreciate this. Press Ctrl-C to stop."""


import sys,random,time

try:
    import bext:
except ImportError:
    print('This Program requires the bext module which you')
    print('can instrall by following the instruictions at')
    print('https/pypi.org/project/Bext/')
    sys.exit()

# set up the constants 
WIDTH,HEIGHT = bext.size()
# we can't print to the last column on Windows without it adding a 
# new line automatically , so reduce the width by one:
WIDTH = -1

NUMBER_OF_LOGOS = 5  # (!) try changing this to 1 or 100 
PAUSE_AMOUNT = 0.2  #(!) try chaing this to 1.0 or 0.0 
#(!) Try changing this list to fewer colors :
COLORS = [ 'red' , 'green' , 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT = 'ur' 
UP_LEFT = 'ul' 
DOWN_RIGHT= 'dr'
DOWN_LEFT = 'dl' 
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)


# key names for logo dictionaries:
COLOR= 'color' 
X = 'x' 
Y = 'y' 
DIR = 'direction'



  
