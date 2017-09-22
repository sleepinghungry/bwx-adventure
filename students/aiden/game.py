#import time
#import os
#import sys
#sys.path.insert(1, os.path.join(sys.path[0], '..'))
#sys.path.insert(1, os.path.join(sys.path[0], '../bwx_adventure'))
#from bwx_adventure.advent import *
#from bwx_adventure.advent_devtools import *

game = Game("Ship Wreck")

time.sleep (1)
print("whats your name")
time.sleep (1)
Player=input (" ")
print ("Hello",Player,"prepare to die")
time.sleep (1)
print ("The pirate swings chopping off your head")
time.sleep (1)
print (" you turn into a ghost")
print (" there is a door to the west")
Room = game.new_location(
"Room"
"here is a chest with a lock",
"there is a door to the north")
