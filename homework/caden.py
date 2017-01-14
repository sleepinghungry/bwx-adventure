#!/user/bin/python
# vim: et sw=2 ts=2 sts=2
#
# This is a tutorial for writing Interactive Fiction with the BWX Adventure Game Engine.
# Ignore the magic before this point (feel free to ask if you are curious).
#
# First we need to import everything we need from the Game engine (a module called 'advent'):

# Allows access to the bwx_adventure module
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from bwx_adventure.advent import *
# for cloud9
from bwx_adventure.advent import Game, Location, Connection, Object, Animal, Robot, Pet, Player
from bwx_adventure.advent import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION

game = Game("Brightworks Adventure")


#############################################################
# HOMEWORK STARTS HERE
#
# 1. Open locations_list.txt and keep it open next to this file.
# 2, Use the locations in locations_list.txt to
#    Write 4 new location commands
#          3 new connection commands, and
#          1 command to create a player
#
# 
##### REMEMBER: commands have () after them
#####           info needed by the command is put inside the ()
#####           If more than one piece of info is needed, separate the pieces of info with a comma.
#
#
# Handy Dandy Reference:
#  https://github.com/sleepinghungry/wwif/wiki/Locations-and-Connections-Homework
#

#####################
# START CODING HERE #
#####################

game.new_location("In Front of Yellow Building",
"There is a bright yellow building to the north, its door wide open.  The only sounds you hear come from the chirping birds around you.")

game.new_location("Vestibule", 
"A kinda dark drabby brown looking area.  There is a door to the east leading to an office and a staircase leading up.")

game.new_location("Upstairs Hallway", 
"Three doors to the north, south, and east are accessible from this hallway.")

game.new_location("Office",
"There is a mess of papers scattered on the floor.  A broken computer screen lies on a desk.")

office=game.new_location
game.run()
