from basic_context import BasicGameWorld
from basic_context import BasicGameEngine
from basic_context import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION
from basic_context import Object, Food, Drink, Container

world = BasicGameWorld()

front_of_office = world.create_location("Candyland","You are standing in front of a huge gingerbread house complete with a wafer roof, butterscotch windows, and candy cane trim.")

vestibule = world.create_location(
  "Candyland",
    """A small area at the bottom of a flight of stairs.
There is a glass door to the west.""")



vestibule.create_object("lollipop", "a rainbow swirly lollipop the size of your face")



world.create_connection("Bubblegum", front_of_office, vestibule, [IN, EAST], [OUT, WEST])

game = BasicGameEngine(world)
game.run()
