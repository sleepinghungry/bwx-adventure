from basic_context import BasicGameWorld
from basic_context import BasicGameEngine
from basic_context import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION

world = BasicGameWorld()

front_of_office = world.create_location("Front of Office","You are standing in front of a bright yellow building.")

vestibule = world.create_location(
  "Vestibule",
    """A small area at the bottom of a flight of stairs.
There is a glass door to the west.""")

world.create_connection("Glass Door", front_of_office, vestibule, [IN, EAST], [OUT, WEST])

game = BasicGameEngine(world)
game.start()
