from basic_context import BasicGameWorld
from basic_context import BasicGameEngine
from basic_context import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION
from basic_context import Object, Food, Drink, Container

world = BasicGameWorld()

bedroom = world.create_location("Bedroom", "a typical messy 41-year old's room")

street = world.create_location("street", "a dark gloomey street")

hallway = world.create_location("Hallway", "a dark long lonely hallway")

door = world.create_connection("Bedroom Door", bedroom, hallway, SOUTH, NORTH)

door = world.create_connection("front door", hallway, street, WEST, EAST)

key = bedroom.create_object("key", "a heavy shiny gold key")

door.make_requirement(key)

mom = world.create_actor("mom", hallway)

world.create_actor("

game = BasicGameEngine(world)
game.run()
