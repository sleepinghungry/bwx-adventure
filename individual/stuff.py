import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
sys.path.insert(1, os.path.join(sys.path[0], '../bwx_adventure'))
from bwx_adventure.advent import *
from bwx_adventure.advent_devtools import *
game = Game("Willow Of Death")
blacktop = game.new_location("hi",
                             "lol")
forest1 = game.new_location(
  "underwater",
  """you are under water.""")
  
forest2 = game.new_location(
  "underwater",
  """you are under water.""")

forest3 = game.new_location(
  "underwater",
  """you are under water.""")
  
shack = game.new_location(
  "underwater",
  """you are under water""")
  
creek = game.new_location(
  "underwater",
  """you are under water.""")

game.new_connection("Forest Path", blacktop, forest1, [NORTH], [NOT_DIRECTION])

game.new_connection("Forest Path", forest1, forest2, [WEST], [EAST])

game.new_connection("Forest Path", forest1, forest3, [NORTH], [NOT_DIRECTION])

game.new_connection("Forest Path", forest1, shack, [EAST], [WEST])                 

game.new_connection("Foest Path", forest2, shack, [NORTH_WEST], [SOUTH_EAST, SOUTH])

game.new_connection("Forest Path", forest2, forest3, [NORTH], [NOT_DIRECTION])

game.new_connection("Forest Path", shack, forest3, [NORTH], [NORTH])

game.new_connection("Forest Path", forest3, creek, [NORTH_EAST], [SOUTH, SOUTH_WEST])

game.new_connection("Forest Path", forest2, blacktop, [SOUTH], [NOT_DIRECTION])

game.new_connection("Forest Path", forest1, forest1, [SOUTH], [SOUTH])

game.new_connection("Forest Path", forest2, forest2, [WEST], [WEST])

game.new_connection("Forest Path", shack, shack, [SOUTH], [SOUTH])

game.new_connection("Forest Path", shack, shack, [EAST], [EAST])

game.new_connection("Forest Path", forest3, forest3, [SOUTH], [SOUTH])
