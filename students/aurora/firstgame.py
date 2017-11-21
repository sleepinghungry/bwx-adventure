from basic_context import BasicGameWorld
from basic_context import BasicGameEngine
from basic_context import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION

world = BasicGameWorld()

front_of_office = world.create_location("Front of Office","You are standing in front of a bright yellow building with a red tin in the grass.")
candyland = world.create_location("candyland","everything is made out of candy")
school = world.create_location("school", "a sunny red building with a swing set")
home = world.create_location("home", "a cozy wooden cottage")
cirqu = world.create_location("cirqu", "a tall biuldind with silks,trapizes,hoops, and ropes hanging from the ceiling")
world.create_connection("tunnel", front_of_office, school, [IN, DOWN], [OUT, UP]) 
world.create_connection("Glass Door", front_of_office, candyland, [IN, EAST], [OUT, WEST])
world.create_connection("stairs", school, home, [IN, NORTH], [OUT, SOUTH])
world.create_connection("portal", home,candyland, [IN, WEST], [OUT, EAST])
world.create_connection("ramp", school,cirqu, [IN, NORTH_WEST], [OUT, SOUTH_EAST])
world.create_connection("door", home, front_of_office, [IN, NORTH],[OUT, SOUTH])
world.create_connection("revoulving door", home,cirqu, [IN, NORTH_WEST]                                                                   
home.create_container("chest", "a gold loked chest with rubys inside")

front_of_office.create_container("cookie tin", "a round red tin with one lonesome cookie")
game = BasicGameEngine(world)
game.run()
