from basic_context import BasicGameWorld
from basic_context import BasicGameEngine
from basic_context import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION

world = BasicGameWorld()

front_of_office = world.create_location("Front of Office","You are standing in front of a bright yellow building.")

candyland = world.create_location("candyland","everything is made out of candy")
school = world.create_location("school", "a sunny red building with a swing set")
home = world.create_location("home", "a cozy wooden cottage")
world.create_connection("tunnel", front_of_office, school, [IN, DOWN], [OUT, UP]) 
world.create_connection("Glass Door", front_of_office, candyland, [IN, EAST], [OUT, WEST])
world.create_connection("stairs", school, home, [IN, NORTH], [OUT, SOUTH])
world.create_connection("portal", home,candyland, [IN, BACK], [OUT, FORWARED])
game = BasicGameEngine(world)
game.run()
