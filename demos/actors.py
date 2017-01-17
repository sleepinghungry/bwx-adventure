#!/user/bin/python
# vim: et sw=2 ts=2 sts=2

# Demo file for adding actors to a game.
# Add the following commands to the file during a class demonstration
#  - Actor() command
#  - set_location() command
#  - add_phrase() command with Say()
#  - add_phrase() command with Verb()
#  - Animal() command
#  - set_allowed_locations() command

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

# Actors

# show creation of a single Actor that stays in one location Actor()




# Show adding a phrase to that actor.  (Same as adding a phrase to an item)




# Show adding adding phrase with Verb to actor.




# Show creation of actor that moves to multiple locations.



# Fini

game.run()
