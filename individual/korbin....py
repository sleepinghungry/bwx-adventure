#!/user/bin/python
# vim: et sw=2 ts=2 sts=2
#
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from bwx_adventure.advent import *
from bwx_adventure.advent import Game, Location, Connection, Object, Animal, Robot, Pet, Player
from bwx_adventure.advent import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION

game = Game("Lucky Day")

sidewalk = game.new_location(
  "Sidewalk",
  "There is a large glass door to the east. The sign says 'Come In!'")

vestibule = game.new_location(
  "Vestibule",
""" There is a house to the north.""")

game.new_connection("Glass Door", sidewalk, vestibule, [IN, EAST], [OUT, WEST])

player = game.new_player(sidewalk)

house = game.new_location ("House",
                           """you can see a small light coming through a door to the east""")



game.new_connection ("Door to house", vestibule, house, [IN, NORTH], [OUT, SOUTH])

kithen = game.new_location ("kithen",
                          """hi""") 

game.new_connection("atic", house, kithen, [UP], [NOT_DIRECTION])


game.run ()

