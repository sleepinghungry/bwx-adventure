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
There is a glass door to the west and door to the south.""")

office = game.new_location(
  "Office",
"""A nicely organized office.
There is a door to the north.""")

game.new_connection("Glass Door", sidewalk, vestibule, [IN, EAST], [OUT, WEST])

player = game.new_player(sidewalk)



# Now lets add a Robot.  Robots are characters in the game that only
# act when you tell them to.  Robots can do anything the player can do.
# You tell them to act by typing their name, a colon, and the command
# want them to perform.  For example:
# > Robby: take key
# > Robby: go in
# > Robby: look
robby = Robot("Robby")
robby.set_location(sidewalk)

# custom phrases available when Robby is present.
# for example: "hi Robby"
robby.add_phrase("hi Robby",

                 Say("Robby sighs metalically and says, \"hello, my name is Robby.\"."))

# Now lets add a Pet.  Pets are like Animals because they move around
# and do things on their own, but they are also like Robots, because
# you can tell them to do anything a player can do.
# try these commands on the cat:
# > tell cat follow
# > pet cat
# > tell cat bark
# > tell cat stay
cat = Pet("cat")
cat.set_location(sidewalk)

chainsaw = sidewalk.new_object("chainsaw", "a big fat chainsaw")

gun = sidewalk.new_object("gun", "a small gun")

player = game.new_player(sidewalk)
game.run()

game.new_connection("Glass Door", sidewalk, vestibule, [IN, EAST], [OUT, WEST])
game.new_connection("Office Door", vestibule, office, [IN, SOUTH], [OUT, NORTH])
