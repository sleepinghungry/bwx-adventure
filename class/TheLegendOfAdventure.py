#!/user/bin/python
# vim: et sw=2 ts=2 sts=2
#
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from bwx_adventure.advent import *
from bwx_adventure.advent import Game, Location, Connection, Object, Animal, Robot, Pet, Player
from bwx_adventure.advent import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION

game = Game("The Legend of Adventure")

#Willowwind game part

driveway = game.new_location(
  "Driveway",
  "You see a large field to the West and a parking lot to the North")

parkinglot = game.new_location(
  "Parking Lot",
"""You are in a parking lot. You see a playground to the North and a driveway to the South""")

foodforest = game.new_location(
"Food_Forest",
"""You are in the food forest you can see garden beds all around you but the office to the 
north""")

office = game.new_location(
"Office",
"""You are in the office with a staircase leading upstairs""")

field = game.new_location(
"Field",
"""You are in a field with grass as tall as your knees and you can see a garden in the distance""")

garden = game.new_location(
"Garden",
"""You are in a garden with an apple on the ground""")

playground = game.new_location(
"Playground",
"""You are now at a playground with a black top in front of you""")

blacktop = game.new_location(
"Blacktop",
"""You are now on the black top you see a shed in the far distance and a large barn next to you""")

room4 = game.new_location(
"Room 4",
"""You are now in the room 4 classroom there is a ruler and test on the teacher's desk""")

computerlab = game.new_location(
"Computer lab",
"""You are now in the computer room with computers all around you""")

room5 = game.new_location(
"Room 5",
"""You are in room 5 you can see a face down piece of paper on the ground""")

room6 = game.new_location(
"Room 6",
"""You are in room 6, there is a match box on the ground and a piece of paper that appears to be a math test""")

barn = game.new_location(
"Barn",
"""you are in a barn with a stage in the back""")

shack = game.new_location(
"Shack",
"""You're in a shack""")

porch = game.new_location(
"Porch",
"""You are on a porch""")
 

#WW game connections
game.new_connection("Pathway", driveway, parkinglot, [IN, NORTH], [OUT, SOUTH])

game.new_connection("pathway2", driveway, field, [IN, WEST], [OUT, EAST])

game.new_connection("gardenpath", field, garden, [IN, NORTH], [OUT, SOUTH])

game.new_connection("toplayground", parkinglot, playground, [IN, NORTH], [OUT, SOUTH])

game.new_connection("playgroundtoblacktop", playground, blacktop, [IN, NORTH], [OUT, SOUTH])

game.new_connection("blacktoptocomputerlab", blacktop, computerlab [IN, NORTH_EAST], [OUT, SOUTH_WEST])

game.new_connection("blacktoptoroom4", blacktop, room4 [IN, EAST], [OUT, WEST])

game.new_connection("playgroundtoporch", playground, porch [IN, WEST], [OUT, WEST])

game.new_connection("playgroundtofoodforest",playground, foodforest [IN, WEST], [OUT, EAST])

game.new_connection("parkinglottofoodforest",parkinglot, foodforest [IN, NORTH_EAST], [OUT,SOUTH], [OUT,SOUTH_WEST])

game.new_connection("foodforesttooffice" , foodforest, office [IN, NORTH], [OUT, SOUTH])

game.new_connection("playgroundtooffice", playground, office [IN, NORTH_EAST], [OUT, SOUTH_WEST])

game.new_connection("officetospplyroom", office, sppulyroom, [IN, UP], [OUT, DOWN])

game.new_connection("spplyroomtoteacherroom", spplyroom, teacherroom,[IN, EAST], [OUT, WEST])

game.new_connection("porchtobarn", porch, barn, [IN, NORTH], [OUT, SOUTH])

game.new_connection("blacktoptobarn", blacktop, barn, [IN, WEST], [OUT, EAST])

game.new_connection("

game.new_connection("

#maze game connections

game.new_connection("

game.new_connection("

game.new_connection("

game.new_connection("                    

#WW game objets


#end of willow Wind
#------------------
#start of the MINE

Central mine = game.new_location(
"
Mineroom1 = game.new_location(
"
Mineroom2 = game.new_location(
"
Mineroom3 = game.new_location(
"
Mineroom4 = game.new_location(
"
E/WTunnel = game.new_location(
"
Blockedroom = game.new_location(
"
Cyclopsroom = game.new_location(
"
breakroom = game.new_location(
"
Dimtunnel = game.new_location(
" 
Keyroom = game.new_location(
"
Storageroom4 = game.new_location(
"
Gemroom = game.new_location(
"
Mineshaftelevatorroom = game.new_location(
"
Warmroom = game.new_location(
"
Generatorroom = game.new_location(
"
Loudroom = game.new_location(
"
Maintenanceroom = game.new_location(
"
Goldroom = game.new_location(
"
Minecartroom = game.new_location(
"
Storageroom3 = game.new_location(
"
Mineshaft
"Mine Shaft"
smallroom = game.new_location(
"small Room"    
Glowingroom = game.new_location(
"Glowing Room"
Magiclanternroom = game.new_location(
"Magic Lantern Room"
Darkroom = game.new_location(
"Dark Room"
Storageroom2 = game.new_location(
"Storage Room 2"
Damproom = game.new_location(
"Damp Room"
Helmetroom = game.new_location(
"Helmet Room"
Widetunnel = game.new_location(
"Wide tunnel" 
Minekitchen = game.new_location(
"Mine kitchen"
Supplyroom = game.new_location(
"Supply Room"
Coatroom = game.new_location(
"Coat Room" 
Largeroom = game.new_location(
"Large Room"
Storageroom1 = game.new_location(
"Storage Room 1
Goblinroom = game.new_location(
"Goblin Room"
Coldroom = game.new_location(
"Cold Room"
Mineexit = game.new_location(
"Mine Exit"
                    

                    


player = game.new_player(driveway)

game.run()














