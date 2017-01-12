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

out_of_village = game.new_location(
  "out_of_Village",
  "Out of the village Nothing is happening!'")
key = sidewalk.new_object("key", "a small tarnished key")

village  = game.new_location(
  "Village",
"in the village it is loud ")

house  = game.new_location(
  "house",
"It is dark.")

game.new_connection("Glass Door", out_of_village, village, [IN, EAST], [OUT, WEST])

player = game.new_player(out_of_village)

key = sidewalk.new_object("key", "a small tarnished key")

office_door.set_flag('locked')
def pick_lock(game, thing):
  game.output("you slip the hairpin into the lock and skillfully pick it open")
  thing.unset_flag('locked')
office_door.add_phrase('pick lock', pick_lock, [hairpin])

def flip_coin(game, thing):
  if random.random() > 0.5:
    game.output("The coin shows heads.");
  else:
    game.output("The coin shows tails.");

game.run()
