#!/user/bin/python
# vim: et sw=2 ts=2 sts=2
#
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from bwx_adventure.advent import *
from bwx_adventure.advent import Game, Location, Connection, Object, Animal, Robot, Pet, Player
from bwx_adventure.advent import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION

game = Game("The Legend of Adventure")

driveway = game.new_location(
  "Driveway",
  "You see a large field to the West and a parking lot to the North")

parkinglot = game.new_location(
  "Parking Lot",
"""You are in a parking lot. You see a playground to the North and a driveway to the South""")

foodforest = new.game_location(
"Food_Forest",
"""You are in the food forest you can see garden beds all around you but the office to the 
north""")

office = new.game_location(
"Office",
"""You are in the office with a staircase leading upstairs""")

field = game.new_location(
"Field",
"""You are in a field with grass as tall as your knees and you can see a garden in the distance""")

garden = game.new_location(
"Garden",
"""You are in a garden with an apple on the ground""")

playground = game.new_location(
"Playground",
"""You are now at a playground with a black top in front of you""")


blacktop = game.new_location(
"Blacktop",
"""You are now on the black top you see a shed in the far distance and a large barn next to you""")

room4 = game.new_location(
"Room 4",
"""You are now in the room 4 classroom there is a ruler and test on the teacher's desk""")

computerlab = new.game_location(
"Computer lab",
"""You are now in the computer room with computers all around you""")

room5 = new.game_location(
"Room 5",
"""You are in room 5 you can see a face down piece of paper on the ground""")

room6 = new.game_location(
"Room 6",
"""You are in room 6, there is a match box on the ground and a piece of paper that appears to be a math test""")

barn = game.new_location(
"Barn",
"""you are in a barn with a stage in the back""")

shack = new.game_location(
"Shack",
"""You're in a shack""")

 

#game connections
game.new_connection("Pathway", driveway, parkinglot, [IN, NORTH], [OUT, SOUTH])

game.new_connection("pathway2", driveway, field, [IN, WEST], [OUT, EAST])

game.new_connection("gardenpath", field, garden, 


player = game.new_player(driveway)


game.run()










