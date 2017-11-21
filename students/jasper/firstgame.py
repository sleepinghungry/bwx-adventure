from basic_context import BasicGameWorld
from basic_context import BasicGameEngine
from basic_context import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION
from basic_context import Object, Food, Drink, Container

world = BasicGameWorld()

bedroom = world.create_location("Bedroom", "a typical messy 41-year old's room")

street = world.create_location("street", "a dark gloomey street")

hallway = world.create_location("hallway", "a dark long lonely hallway")

cellar = world.create_location("cellar", "a dark moist musty cellar")

fals_panel = world.create_location("false_panel", "dark and creepy")
door = world.create_connection("cellar DOOR", false_panel, cellar, SOUTH, NORTH)

door = world.create_connection("Bedroom Door", bedroom, hallway, SOUTH, NORTH)




door = world.create_connection("false_panel",false_panel,bedroom,SOUTH, NORTH)

door = world.create_connection("front door", hallway, street, WEST, EAST)

key = bedroom.create_object("key", "a heavy shiny gold key")

door.make_requirement(key)

mom = world.create_actor("mom", hallway)

key = hallway.create_object("key", "a light shiny silver key")

key = street.create_object("key", "a dark brown from the 60s key")


game = BasicGameEngine(world)
game.run()
