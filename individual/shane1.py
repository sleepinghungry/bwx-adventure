
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from bwx_adventure.advent import *

from bwx_adventure.advent import Game, Location, Connection, Object, Animal, Robot, Pet, Player
from bwx_adventure.advent import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION

game = Game("World Warp-Z")

local_1 = game.new_location(
  "Office Door",
  "There is a door that has red stains on the handle, to the East.")

Death = game.new_location(
  "Dark Alley",
"""If you go west you will get eaten by the Hord.""")



game.new_connection("Glass Door", Local_1, Death, [IN, ], [OUT, WEST])



player = game.new_player(Local_1)


game.run()
