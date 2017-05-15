import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from bwx_adventure.advent import *
from bwx_adventure.advent import Game, Location, Connection, Object, Animal, Robot, Pet, Player
from bwx_adventure.advent import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION

game = Game("Death Hollows")

cellar = game.new_location("Cellar",
                  "There are lots of spider webs around you. And to the east there is a closet")

cellar_closet = game.new_location(
    "Closet",
    "THis is a small closet, there is a key here.")

game.new_connection("Closet cellar", cellar, cellar_closet, [IN, EAST], [OUT, WEST])

player = game.new_player(cellar)

playername = input("What is your name...?")
print(playername, "Well you are blind, and I'm here to help you...")
imhere = input("Do you remember you mission...?")
print("Well", playername, "I highly doubt you do... you were unconcious for a week...")
print("Well you're stuck in this mansion till you find a man named Dan Hollows... find him... get him out alive and earn freedom...")
print("Good Luck")

game.run()
