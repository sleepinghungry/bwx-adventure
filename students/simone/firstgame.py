from basic_context import BasicGameWorld
from basic_context import BasicGameEngine
from basic_context import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION
from basic_context import Object

world = BasicGameWorld()

candyland = world.create_location("candyland","You are standing in front of a huge gingerbread house complete with a wafer roof, butterscotch windows, and candy cane trim.")

candyland.create_object("key", "large brown key made of chocolate")
healthyland = world.create_location(
    "healthyland"
    """a bigger land full of gross healthy foods like broccoli trees and lakes full of steaming carrot stew. It is snowing large clumps of squash now, and there is no other way to go but down with the snow """)

world.create_connection("bridge", candyland, healthyland, [IN, UP], [OUT, DOWN])

canned_liver_palace = world.create_location("canned liver palace", "the squash snow takes you down just as a broccoli tree slams to the ground inches from your body. You begin falling into blackneness
