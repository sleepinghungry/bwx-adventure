#!/user/bin/python
# vim: et sw=2 ts=2 sts=2
#
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from bwx_adventure.advent import *
from bwx_adventure.advent import Game, Location, Connection, Object, Animal, Robot, Pet, Player
from bwx_adventure.advent import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION

game = Game("Lky day")

sidewalk = game.new_location(
  "Eye of a snow storm",
  "it is 

vestibule = game.new_locatione
  "Eye of a sand storm ",
it is vary sandy.


game.new_connection("Glass Door", sidewalk, vestibule, [IN, EAST], [OUT, WEST])

player = game.new_player(sidewalk)

game.run()
