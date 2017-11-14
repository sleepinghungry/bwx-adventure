from basic_context import BasicGameWorld
from basic_context import BasicGameEngine
from basic_context import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION

world = BasicGameWorld()

front_of_office = world.create_location("Front of Office","You are standing in front of a bright yellow building.")
up_stairs = world.create_location("upstairs","Spooky atic, filled with dusty boxs and a small broken window to the east.")

vestibule = world.create_location(    
  "Vestibule",
    """A small area at the bottom of a flight of stairs.
There is a ladder going up.""")
world.create_connection("Glass Door", front_of_office, vestibule, [IN, EAST], [OUT, WEST])

world.create_connection("Ladder", up_stairs, vestibule, [UP, SOUTH])


game = BasicGameEngine(world)
game.run()
