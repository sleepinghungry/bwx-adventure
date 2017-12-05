import time
from basic_context import BasicGameWorld, Location, Connection
from basic_context import BasicGameEngine
from basic_context import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION
from basic_context import Object, Food, Drink, Container

world = BasicGameWorld()



vestibule = world.create_location(
"Vestibule",
 """Trees rush by as the train slows down. """)

train_station = world.create_location("Train station", "The Train is behind you and a large door to the north.")

room_in_station = world.create_location("room in station", "A Shop to the right and rows of seats infrount of you, and hallway in the north eastern part of the back.")

hallway = world.create_location("long hallway.","To the right is the owners office it may be unlocked, at the end of the hallway is a door with a sign that says KEEP OUT.")

locked_office = world.create_location("Dark office", "File cabnents and a safe on the desk you need a key to open this.")

keep_out= world.create_location("room with a guard""a pile of money is sitting in the room a guard is sleeping to the right")

Deck= world.create_location("Deck","this is an old deck with creaking floor boards.")

Main_deck= world.create_location("Main deck","you can see pirates all around and caring big jugs of mead.")

Captains_room= world.create_location("Captains room","No one is in here but you")

world.create_connection("Door1", vestibule, train_station, [IN, EAST], [OUT, NORTH])
world.create_connection("Door2", train_station, room_in_station, [IN, WEST], [OUT, WEST])
world.create_connection("Door3", room_in_station, hallway, [IN, EAST], [OUT,NORTH])
world.create_connection("Door4", hallway, locked_office , [IN, WEST], [OUT, SOUTH,])
world.create_connection("Door5", locked_office, keep_out , [IN,WEST], [OUT, UP])
world.create_connection("Door6", Staircase, Deck, [IN,EAST], [OUT,EAST])
world.create_connection("Door7", Deck,Main_deck ,[IN,EAST,], [OUT,WEST,])
world.create_connection("Door8",Captains_room, [IN,EAST,], [OUT,WEST,])

Key = hallway.create_object ("key","a heavy shiny gold key")
Sword = Armor_room.create_object ("sword","a nice big sword with jewels ")
Armor = Armor_room.create_object ("armor","an armor chest plate made of silver ")



game.end()
































