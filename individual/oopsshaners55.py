import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
sys.path.insert(1, os.path.join(sys.path[0], '../bwx_adventure'))
from bwx_adventure.advent import *
from bwx_adventure.advent import Game, Location, Connection, Object, Animal, Robot, Pet, Player, Say
from bwx_adventure.advent import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION
import bwx_adventure.advent_devtools
import random


game = Game("Willow ooOf Death")

terrorrized = game.new_location(
     "You Die Here",
     "The END!!!:)")
player = game.new_player(terrorrized)

game_over_location = game.new_location(
    "You Are Dead",
    "Sorry, you have died.  There's nowhere to go except to exit the program.")

game.new_connection("Game Over", terrorrized, game_over_location, [IN, OUT, NORTH, EAST, WEST, SOUTH, NORTH_EAST, NORTH_WEST, SOUTH_EAST, SOUTH_WEST], [NOT_DIRECTION]) 

talk_to_ft = False

fortune_teller = Actor("Fortune teller")
fortune_teller.set_location(terrorrized)

def talk_to_ft(game,thing):
    global terrorrized
    talk_to_ft = True
    playerftanswer = input("Would you like me to tell you your fortune...?")
    if playerftanswer == "Y":
        game.output("Your future is that you are stuck in this room forever..."
                    "you will either quit... or restart...(:")
    else:
        game.output("Yor loss... tell me when you want to know...")

fortune_teller.add_phrase(["talk to fortune teller", "talk to ft"], talk_to_ft)

