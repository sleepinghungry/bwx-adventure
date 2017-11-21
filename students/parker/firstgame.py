from basic_context import BasicGameWorld
from basic_context import BasicGameEngine
from basic_context import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION

world = BasicGameWorld()

# Hi Parker, Eping here.  I added quotes in this line of code so it would work:
#dungeon = world.create_location("Virgonia Isle, in the dungeon")
dungeon = world.create_location("Virgonia Isle", "in the dungeon")

Espilcen = world.create_location ("Espilcen dungeon cell", " you are standing in a dark, musty dungeonn cell. you musty get out!")

world.create_connection("dungeon cell", dungeon, Espilcen, [IN, EAST], [OUT, WEST])
  
air_vent = dungeon.create_object("air vent", "there is a air vent in the stone ceiling")

metal = dungeon.create_object("metal", "you see a piece of metal on the ground")

# So...your key can only be a requirement for a location or a connection.  It can't
# be a requirement for another object.  I'd recommend making your air_vent a
# connection between Espilcen and a new location.

game = BasicGameEngine(world)
game.run()
