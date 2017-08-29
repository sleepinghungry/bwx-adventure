#!/user/bin/python
# vim: et sw=2 ts=2 sts=2

# Demo file for adding user-defined functions to a game.
# Add the following commands to the file during a class demonstration
#  - Actor() command
#  - set_location() command
#  - add_phrase() command with Say()
#  - add_phrase() command with Verb()
#  - Animal() command
#  - set_allowed_locations() command
#  - don't forget the game.add_actor commands

import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from bwx_adventure.advent import Game, Location, Connection, Object, Animal, Robot, Pet, Player, Actor, Verb, Say, SayOnNoun, SayOnSelf, Container, Food, Drink, Die
from bwx_adventure.advent import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION

game = Game("Willow Wind Adventure Demo")

# Locations
front = game.new_location("Front of Yellow Building", "There is a bright yellow building here.")
vestibule = game.new_location("Vestibule","This is a brown drab room.  There are stairs leading up, and an door leading to an office.")
office = game.new_location("Office", "This place is a mess.")
upstairs = game.new_location("Upstairs Hall", "You are upstairs")

# Connections
front_door = game.new_connection("Front Door",front, vestibule, IN, OUT)
office_door = game.new_connection("Office Door", vestibule, office, IN, OUT)
stairs = game.new_connection("Upstairs", vestibule, upstairs, UP, DOWN)

# Player
player = game.new_player(front)

# Items
ball = front.new_object("ball","a bouncy red rubber ball")
ball.add_phrase("bounce ball", Say("This is fun!"))

key = upstairs.new_object("key","a worn out bronze key")
office_door.make_requirement(key)

principal = Actor("principal")

principal.set_location(office)
principal.health = 3

def final_words(game, thing):
  thing.health -= 1
  if thing.health == 2:
    game.output("The principal looks severely injured. She says, \"I'm glad someone made it out alive.\"")
  elif thing.health == 1:
    game.output("The principal closes her eyes and struggles to whisper, \"There are supplies.  You can find them.\"")
  elif thing.health == 0:
    game.output("The principal's last words are: \"I should have been a game designer.\"")
  elif thing.health < 0:
    game.output("The principal has died.") 


principal.add_phrase("chat", final_words)

soldier = Animal("soldier of fortune")
soldier.set_location(upstairs)
soldier.set_allowed_locations([office, vestibule, upstairs])

game.add_actor(soldier)
game.add_actor(principal)


game.run()


