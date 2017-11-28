from basic_context import BasicGameWorld
from basic_context import BasicGameEngine
from basic_context import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION
from basic_context import Object, Food, Drink, Container

world = BasicGameWorld()

hospital_room_105 = world.create_location("hospital room 105", "a dark hospital room #105 with a fliker of light and a dead corps rotting in the corner")
a_dead_corps = hospital_room_105.create_container("a dead corps", "a rotting dead corps sitting in the corner")

long_hospital_hallway = world.create_location("long hospital hallway", "dark long hallway with a flikering light to the west and nothing but silence to the east")
world.create_connection("hard oak door", hospital_room_105,long_hospital_hallway, SOUTH, NORTH)

janetors_closet = world.create_location("janetors closet", "dark quiet and looks like thier might be a secret panel at the end of he room")
sergins_glove = janetors_closet.create_object("sergins glove", "sergins glove a dark read wall it drips its read blood slowlly onto the floor")











a_dead_corps.make_requirement([sergins_glove, scalpal])
game = BasicGameEngine(world)
game.run()
