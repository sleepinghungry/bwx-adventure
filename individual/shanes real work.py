
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from bwx_adventure.advent import *

from bwx_adventure.advent import Game, Location, Connection, Object, Animal, Robot, Pet, Player
from bwx_adventure.advent import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION

game = Game("World Warp-Z")

office = game.new_location(
  "Office",
  "You are in the office. The door shus behind you, you are locked in.")

Death = game.new_location(
  "Dark Alley",
"""If you go South you will get eaten by the Hord.""")
game.new_connection("office door", , , [IN, ], [OUT, ])

office.add_object("key pair",
                          "this is a small bronze key, maybe used to open something.")


player = game.new_player(Local_1)


game.run()
