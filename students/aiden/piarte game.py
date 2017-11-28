import time
from basic_context import BasicGameWorld, Location, Connection
from basic_context import BasicGameEngine
from basic_context import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION
from basic_context import Object, Food, Drink, Container

world = BasicGameWorld()




print("what's your name")
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

hallway = world.create_location("Hallway", "There is a empty hallway with a key on the ground. you can go East.")

feast_hall = world.create_location("Feast Hall", "There are a bunch of pirates here laughing and having a good time. there is an exit south.")

Armor_room = world.create_location("Armor room","Here is a dark room with swords and armor.")

Staircase= world.create_location("stair case","this is a rickety old staircase.")

Deck= world.create_location("Deck","this is an old deck with creaking floor boards.")

Main_deck= world.create_location("Main deck","you can see pirates all around and caring big jugs of mead.")

Captains_room= world.create_location("Captains room","No one is in here but you")

world.create_connection("Door1", vestibule, room, [IN, EAST], [OUT, NORTH])
world.create_connection("Door2", room, hallway, [IN, WEST], [OUT, WEST])
world.create_connection("Door3", hallway, feast_hall, [IN, EAST], [OUT,NORTH])
world.create_connection("Door4", feast_hall, Armor_room, [IN, WEST], [OUT, SOUTH,])
world.create_connection("Door5", Armor_room,Staircase , [IN,WEST], [OUT, UP])
world.create_connection("Door6", Staircase,, Deck, [IN,EAST], [OUT,EAST])
world.create_connection("Door7", Deck,Main_deck ,[IN,EAST,], [OUT,WEST,])
world.create_connection("Door8",Captains_room, ,[IN,EAST,], [OUT,WEST,])

Key = hallway.create_object ("key","a heavy shiny gold key")
Sword = Armor_room.create_object ("sword","a nice big sword with jewels ")
Armor = Armor_room.create_object ("armor","an armor chest plate made of silver ")




game = BasicGameEngine(world)
game.run()

