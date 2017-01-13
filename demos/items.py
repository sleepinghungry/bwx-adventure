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

game.run()
