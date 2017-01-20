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

forest = game.new_location(
  "forest",
  "you are in a dark forest with a axe that looks like it was form a lumber jack!'")
axe = axe.new_object("axe", "a double bladed axe")

willow_wind  = game.new_location(
  "willow wind",
"you see lots of kids here ")

creek side = game.new_location(
  "creek side",
"there is wierd creek here.")

fantasy forest = game.new_location(
 "fantasy forest"
"there are lots of fantastic monsters here!")

fantasy forest = game.new_location(
  "fantasy forest"
  "it is dark here")

fantasy forest = game.new_location(
  "fantasy forest"
  "a dark forest, there is a key here"

ice world = game.new_location(
   "brrr"

ice world =game.new_location( 
"ice world"

game.new_connection("glass door", forest, willow wind,fantasy forest, [IN, EAST], [OUT, WEST])

player = game.new_player(forest)

key = fantasy forest.new_object("key", "a small tarnished key")

office_door.set_flag('locked')
def pick_lock(game, thing):
  game.output("you slip the hairpin into the lock and skillfully pick it open")
  thing.unset_flag('locked')
office_door.add_phrase('pick lock', pick_lock, [hairpin])

def (game, thing):
  if random.random() > 0.5:
    game.output("The coin shows heads.");
  else:.");game.output("The coin shows tails
game.run()
    
