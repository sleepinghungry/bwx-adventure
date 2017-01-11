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
"""A small area at the bottom of a flight of stairs.
There is a glass door to the east.""")

game.new_connection("Glass Door", sidewalk, vestibule, [IN, EAST], [OUT, WEST])

tortureroom = game.new_location(
    "Midieval Torture Room",
"""You see multiple horrifying torture devices in a small stone brick room.
There is an arched doorway leading into a dark passageway to the West.""")

darkpassageway = game.new_location(
    "Dark Passageway",
"""You can go forward to the North or back into the torture room to the South.""")

game.new_connection("Arched Doorway", tortureroom, darkpassageway [IN, WEST], [OUT, SOUTH])











player = game.new_player(sidewalk)












game.run()
