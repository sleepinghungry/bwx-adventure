import time
from basic_context import BasicGameWorld, Location, Connection
from basic_context import BasicGameEngine
from basic_context import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION
from basic_context import Object, Food, Drink, Container

world = BasicGameWorld()




print("whats your name")
Player=input (" ")
print ("Hello",Player,"prepare to die")
print ("The pirate swings chopping off your head")
time.sleep (1)
print (" you turn into a ghost")

vestibule = world.create_location(
"Vestibule",
 """you are standing in the room you were just killed. You see your lifeless body and want to get revenge.
There is a door to the East.""")

room = world.create_location("Room", "Here is a chest with a lock. there is a door to the West.")

hallway = world.create_location("Hallway", "There is a emtpy hallway with a key on the ground. you can go East.")

feast_hall = world.create_location("Feast Hall", "There are a bunch of piartes here laughting and having a good time. there is an exit south.")



world.create_connection("Door1", vestibule, room, [IN, EAST], [OUT, NORTH])
world.create_connection("Door2", room, hallway, [IN, WEST], [OUT, WEST])
world.create_connection("Door3", hallway, feast_hall, [IN, EAST], [OUT,SOUTH])

Key = hallway.create_object ("key","a heavy shiny gold key")

game = BasicGameEngine(world)
game.run()
