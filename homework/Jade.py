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
desert = game.new_location("desert",
"It is hot and dry with miles of sand")

sea = game.new_location("sea",
"Thousands of fish swim in the blue ocean")

ice = game.new_location("ice world",
"evrey thing is ice and snow")                  

fire = game.new_location("fire world",
"evrey thing is lava and fire")


game.run()
