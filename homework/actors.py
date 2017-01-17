#!/user/bin/python
# vim: et sw=2 ts=2 sts=2

import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from bwx_adventure.advent import Game, Location, Connection, Object, Actor, Animal, Robot, Pet, Player, Say, SayOnNoun, SayOnSelf, Verb, Food, Drink, Container, Die
from bwx_adventure.advent import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION

game = Game("Willow Wind Adventure")

#############################################################
# HOMEWORK STARTS HERE
#
# 1. Add an Actor to the game and attach a special phrase using:
#    1 Actor command
#    1 set_location command
#    1 add_phrase command
#      (something like, "look at _______" and then game describes the character
#       or "talk to _________" and then the game describe the character talking
#       to the player)
#    1 add_actor command
#
# 2. Add an Animal to the game that wanders around the game using
#    1 Animal() command
#    1 set_location command
#    1 set_allowed_locations command
#    1 add_phrase command
#    1 add_actor command
#
# Optional (Advanced): Add a custom action to the character using
#    1 def custom_action definition
#    1 add_phrase command that uses a Verb command instead of a Say command
#
#
# Handy Dandy Step-by-Step Reference:
#  https://github.com/sleepinghungry/wwif/wiki/Handy-Dandy-Guide-to-Actors
#
# Handy Dandy Quick Reference to Everything:
#  https://github.com/sleepinghungry/wwif/wiki/Handy-Dandy-Quick-Reference-Guide-to-Everything
#############################################################

game = Game("Willow Wind Adventure Demo")

# Locations
front = game.new_location("Front of Yellow Building", "There is a bright yellow building north of here.")
vestibule = game.new_location("Vestibule","This is a brown drab room.  There are stairs leading up, and an door leading to an office.")
office = game.new_location("Office", "This place is a mess.")
upstairs = game.new_location("Upstairs Hall", "You are upstairs")

# Connections
front_door = game.new_connection("Front Door",front, vestibule, [IN,NORTH], [OUT,SOUTH])
office_door = game.new_connection("Office Door", vestibule, office, [IN,EAST], [OUT,WEST])
stairs = game.new_connection("Upstairs", vestibule, upstairs, UP, DOWN)

# Player
player = game.new_player(front)

# Items
ball = front.new_object("ball","a bouncy red rubber ball")
ball.add_phrase("bounce ball", Say("This is fun!"))

key = upstairs.new_object("key","a worn out bronze key")
office_door.make_requirement(key)

#####################
# START CODING HERE #
#####################

#################
# END CODE HERE #
################

game.run()
