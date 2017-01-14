#!/user/bin/python
# vim: et sw=2 ts=2 sts=2
#
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from bwx_adventure.advent import *
from bwx_adventure.advent import Game, Location, Connection, Object, Animal, Robot, Pet, Player
from bwx_adventure.advent import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION

game = Game("Shadows")

sewer = game.new_location(
  "Sewer",
  "There is tunnels branching off in nearly all directions, there is a strange noise that seems to come from every direction.")

dungeon = game.new_location(
  "Dark Dungeon Cell",
  "There is a guard just outside your cell with a key chain and a dwarven dagger, the door to your cell is to the north.")

corridor = game.new_location(
  "Corridor",
  "You are in long corridor, there is a large open wooden door to the west.")

tower = game.new_location(
  "Shadowy Tower",
  "A dark tower cloaked in shadows, it seems to be whispering something to you.")

courtyard = game.new_location(
  "Courtyard",
  "You are in a large empty courtyard with dead people littering the floor, there seems to be some kind of lethal disease. There is a large grate to the west that seems movable and a pathway leading north.")

cliff = game.new_location(
  "Cliff Edge",
  "You are on a cliff edge, there is a narrow pathway leading down to the northeast.")

cell_door = game.new_connection("Cell Door", dungeon, corridor, [IN, NORTH], [OUT, SOUTH])

pathway = game.new_connection("Pathway", courtyard, cliff, [IN, NORTH], [OUT, SOUTH])

narrow_pathway = game.new_connection("Narrow Pathway", cliff, tower, [IN, NORTHEAST], [OUT, SOUTHWEST])

wooden_door = game.new_connection("Wooden Door", corridor, courtyard, [IN, WEST], [OUT, EAST])

grate = game.new_connection("Grate", courtyard, sewer, NOT_DIRECTION, [OUT, EAST])

player = game.new_player(dungeon)

guard = Actor("guard")
guard.set_location(dungeon)
guard.set_allowed_locations([dungeon])


torch = Object("torch", "a recently lit torch")
torch = corridor.new_object("torch", "a recently lit torch")

dagger = Object("dwarven dagger", "a polished dwarven dagger")
key_chain = Object("key chain", "a rusty ring of old keys")
cell_door.make_requirement (key_chain)
guard.add_to_inventory(key_chain)
guard.add_to_inventory(dagger)

cell_door.set_flag('locked')
def unlock_door(game, thing):
  game.output("you stick one of the keys on the key chain into the key hole and it clicks open")
  thing.unset_flag('locked')
cell_door.add_phrase('unlock door', unlock_door, [key_chain])

grate.set_flag('locked')
def move_grate(game, thing):
  game.output("you pull the grate out of place and it makes a horrific screech on the stone")
  #thing.unset_flag('locked')
  thing = game.new_connection("Grate", courtyard, sewer, [IN,WEST], [OUT, EAST])
grate.add_phrase('move grate', move_grate, [])

sharp_bone = dungeon.new_object("sharp bone", "a sharp bone lies in the corner to the left of you")

def kill_guard(game, thing):
  if not "sharp bone" in game.player.inventory:
    game.output("You try to attack the guard with your bare hands, but he wacks you with the bunt of his blade.")
    player.terminate()
  else:
    game.output("You stab the guard from behind at the base of his neck, and he drops to the ground dead. The guard had a key chain, a dwarven dagger, and a written parchment, they could be useful.")

    guard.terminate()
    guard.act_drop1(player,"key chain","The guard dropped a key chain.")
    guard.act_drop1(player,"dwarven dagger","The guard dropped a dwarven dagger")
guard.add_phrase("kill guard", kill_guard)

#unset locations


game.run()

