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



name_of_a_location_variable=game.new_location(),"FOREST""this is a forest with trees all around you. an arrow is stuck in a tree
"with a note attached to it that says: ENTER AT YOUR OWN RISK.()
"

name_of_a_location_variable=game.new_location(),"ISLAND""This is an island with ocean all around you. there have been rumors of strage disappearences on this island.()
"

name_of_a_location_variable=game.new_location(),"MOUNTAIN""This is a very tall mountain with a lake around it. You hear the sound of fighting in the distance.()
"

name_of_a_location_variable=game.new_location(),"VOLCANO""This is a volcano that looks like it has been deserted. You freeze as you hear the volcano rumbling.()









game.run()
