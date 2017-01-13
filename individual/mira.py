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

curtain = game.new_location(
  "curtain",
  "there is a shadow of a large animal'")
dress = curtain.new_object(" dress", "an old torn dress")
on_stage = game.new_location(
  "on stage",
"""The strange animal is very real. He tries to kill you """)


microphone = on_stage.new_object("microphone", "a rusty microphone")
under_stage = game.new_location(
  "under stage",
"""You escaped the monster. There is a narrow stair case leading down """)
slipper = under_stage.new_object("slipper", "a pink slipper")
game.new_connection("Glass Door",curtain, on_stage, [IN, EAST], [OUT, WEST])
person = Actor("person")
person.set_location(under_stage)
game.new_connection("Glass Door",on_stage, under_stage, [IN, NORTH], [OUT, SOUTH])
game.new_connection("Glass Door",under_stage, curtain, [UP], [DOWN])

player = game.new_player(curtain)

game.run()
