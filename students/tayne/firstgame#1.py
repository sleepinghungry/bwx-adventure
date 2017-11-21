from basic_context import BasicGameWorld
from basic_context import BasicGameEngine
from basic_context import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION

world = BasicGameWorld()

front_of_office = world.create_location("Front of Office","You are standing in front of a bright yellow building.")

vestibule = world.create_location(
  "Vestibule",
    """A small area at the bottom of a flight of stairs.
There is a glass door to the west.""")

print ("steve: you are clone trooper 3 in an abandoned hotel. its abandoned because there was a blast on the top floor. all we know is that the bad guys are all here. can you go and find them don't worry your not alone.")


world.create_connection("Glass Door", front_of_office, vestibule, [IN, EAST], [OUT, WEST])
                      
elevator = world.create_location("elevator","you are in the elevator.")

door = world.create_connection("elevator door", elevator, [IN, SOUTH], [OUT, NORTH])

print ("theres a key")
                                                           

key = elevator.create("key","a heavy shiny gold key")

print ("steve:press a floor number")

print  ("controles are space= shoot, e=east, s=south, n=north,w=west, p=pickup key")
game = BasicGameEngine(world)
game.run()








