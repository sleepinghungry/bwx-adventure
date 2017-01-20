#!/user/bin/python
# vim: et sw=2 ts=2 sts=2

import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from bwx_adventure.advent import Game, Location, Connection, Object, Actor, Animal, Robot, Pet, Player, Say, SayOnNoun, SayOnSelf, Verb, Food, Drink, Container, Die
from bwx_adventure.advent import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION

game = Game("WIllow Wind Adventure")

#############################################################
# HOMEWORK STARTS HERE
#
# 1. Open locations_list.txt and keep it open next to this file.
# 2. Use the locations in locations_list.txt to
#    Write 4 new location commands
#          3 new connection commands, and
#          1 command to create a player
#
# Use can highlight text and use CTRL-C to copy, and CTRL-V to paste.
#
# Handy Dandy Reference:
#  https://github.com/sleepinghungry/wwif/wiki/Locations-and-Connections-Homework
# Handy Dandy Quick Reference to Everything:
#  https://github.com/sleepinghungry/wwif/wiki/Handy-Dandy-Quick-Reference-Guide-to-Everything
#############################################################

#####################
# START CODING HERE #
#####################


#################
# END CODE HERE #
#################

game.run()
