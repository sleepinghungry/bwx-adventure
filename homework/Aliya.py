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
from bwx_adventure.advent import Game, Location, Connection, Object, Animal, Robot, Pet, Player, Say, SayOnNoun, SayOnSelf
from bwx_adventure.advent import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION

game = Game("Brightworks Adventure")


#############################################################
# HOMEWORK STARTS HERE
#
# 1. Open items_list.txt and keep it open next to this file.
# 2. Use the locations in items_list.txt to
#    Write 2 new object commands (1 ball, 1 key)
#          1 make required commands (key required to open office door)
#          1 add phrase commands (bounce ball)
#
# Handy Dandy Reference:
#  https://github.com/sleepinghungry/wwif/wiki/Handy-Dandy-Guide-to-Items
#
#############################################################

# Locations
front = game.new_location("Front of Yellow Building", "There is a bright yellow building here.")
vestibule = game.new_location("Vestibule","This is a brown drab room.  There are stairs leading up, and an door leading to an office.")
office = game.new_location("Office", "This place is a mess.")
upstairs = game.new_location("Upstairs Hall", "You are upstairs")

# Connections
front_door = game.new_connection("Front Door",front, vestibule, IN, OUT)
office_door = game.new_connection("Office Door", vestibule, office, IN, OUT)
stairs = game.new_connection("Upstairs", vestibule, upstairs, UP, DOWN)

# Player
player = game.new_player(front)

#####################
# START CODING HERE #
#####################
ball = front.new_object("ball","Bouncy round rubber ball")
ball.add_phrase("bounce ball", Say("This is fun!!!"))
key = upstairs.new_object("key","Silver Key")
office.make_requirement(key)
#################
# END CODE HERE #
################

game.run()
