from basic_context import BasicGameWorld
from basic_context import BasicGameEngine
from basic_context import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION
from basic_context import Object, Food, Drink, Container

world = BasicGameWorld()
# YOUR CODE STARTS HERE

bedroom = world.create_location("Bedroom", "a typical messy 41-year old's room")

hallway = world.create_location("Hallway", "a dark long lonely hallway")

world.create_connection("Bedroom Door", bedroom, hallway, SOUTH, NORTH)

bedroom.create_object("key", "a heavy shiny gold key")

mom = world.create_actor("mom", hallway)

# YOUR CODE ENDS HERE
game = BasicGameEngine(world)
game.run()
