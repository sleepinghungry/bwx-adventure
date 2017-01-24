#!/user/bin/python
# vim: et sw=2 ts=2 sts=2
#
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from bwx_adventure.advent import *
from bwx_adventure.advent import Game, Location, Connection, Object, Animal, Robot, Pet, Player
from bwx_adventure.advent import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION


import threading

def worker():
    """"""
    print 'worker'  
    
      import time
        def countdown(n) :
          while n > 0:
           print (n)
             n = n - 1
             if n ==0:
            print("you hear very light foot steps, you feel a chunk of your flesh getting riped of your bone on your leg. You try to move but you can not. You lose your vision. You can no longer think. ")
          countdown(30)
return

threads = []
for i in range(5):
    t = threading.Thread (target=worker)
    threads.append (t)
    t.start ()




game = Game("The Legend of Adventure")



#Willowwind game part

topofdriveway = game.new_location(
  "Top Of Driveway",
  """You are standing at the top of a long driveway leading to what appears to be a school. The school must have once been a farm because one of the buildings is a big red barn. All of the other buildings are yellow. There is a parking lot to the north and a large feild to the west.""")

parkinglot = game.new_location(
  "Parking Lot",
"""You are in the parking lot of the school. You see a playground to the North and a driveway to the South. To the northeast is a food forest.""")

foodforest = game.new_location(
"Food_Forest",
"""You are in the school's food forest. There are lots of fruit trees and other edible foods growing here. There is a apple tree with a juicy looking apple hanging just within reach. There is a parking lot to the southeast and a playground to the west. To the north is a building which appears to be the schools office.""")

office = game.new_location(
"Office",
"""You are in the office of the school. There is a teachers office room to the east and a stairway leading upwards.""")

field = game.new_location(
"Field",
"""You are in a field with grass as tall as your knees. To the west is a driveway and there is a garden to the north.""")

garden = game.new_location(
"Garden",
"""You are in the schools garden. There are garden beds all around and a pile of compost against one fence. There is a feild to the south.""")

playground = game.new_location(
"Playground",
"""You are standing in the schools playground. There you can go north, northeast, east, south, or west.""")

blacktop = game.new_location(
"Blacktop",
"""You are now on the blacktop of the school. You can go in five different directions.""")

room4 = game.new_location(
"Room 4",
"""You are in room 4. It is one of the school's class rooms. There are five tables and a desk in the room. On the desk is a uncomleated science test. The blacktop is to the east.""")

computerlab = game.new_location(
"Computer lab",
"""You are rein the computer lab of the school. There are computers on tables all around the room. The blacktop is to the southwest.""")

room5 = game.new_location(
"Room 5",
"""You are in room 5. One of the schools classrooms. There are tables all around the room and a sofa in the back. On one of the tables is an uncompleated LA test. The porch is to east.""")

room6 = game.new_location(
"Room 6",
"""You are in room 6. One of the school's classrooms. There are tables and a few desks around the room. On the side of the room is a large green sheet of fabric suspended on a frame. It appears to be a greenscreen. Against the wall is an old file cabinet. The porch is to the southeast.""")

barn = game.new_location(
"Barn",
"""You are inside the large red barn. It has been converted into what looks like a space for dancing. In the corner of the room is a drinking fountain and a closet. The porch is to the south and the blacktop is to the east.""")

shack = game.new_location(
"Shack",
"""You're in a shack. There is not much light but you can make out a small machene in the middle of the room. It looks like it is a test grading machene.""")

porch = game.new_location(
"Porch",
"""You are on a porch in front of two classrooms. Room 5 is to the west, and room 6 is to the northwest.""")
 
forest1 = game.new_location(
  "Forest",
  """You are in a forest filled with trees and tall dry grass. It is hard to tell which way is which. Eveything looks the same.""")
  
forest2 = game.new_location(
  "Forest",
  """You are in a forest filled with trees and tall dry grass. It is hard to tell which way is which. Eveything looks the same.""")

forest3 = game.new_location(
  "Forest",
  """You are in a forest filled with trees and tall dry grass. It is hard to tell which way is which. Eveything looks the same.""")
  
forest4 = game.new_location(
  "Forest",
  """You are in a forest filled with trees and tall dry grass. It is hard to tell which way is which. Eveything looks the same.""")
  
creek = game.new_location(
  "Creek",
  """You are standing by a clear creek. You can hear the chirping of birds and trickle of running water. The forest is to the southwest.""")
  
teacheroffice = game.new_location(
  "Teacher's Office",
  """You are in a room in which each of the teachers have a desk. There is a bathroom in the corner and a pencil sharpener on the wall. The office is to the east.""")
supplyroom = game.new_location(
  "Supply Room",
  """You are in an upstairs supply room. There are boxes os school supplies around the edge of the room. The only exit is down the way you came from.""")
#WW game connections
game.new_connection("Driveway", topofdriveway, parkinglot, [NORTH], [SOUTH])

game.new_connection("Path To Field", topofdriveway, field, [WEST], [EAST])

game.new_connection("Path To Garden", field, garden, [NORTH], [SOUTH])

game.new_connection("Gravel Walkway", parkinglot, playground, [NORTH], [SOUTH])

game.new_connection("Food Forest Gate", parkinglot, foodforest, [SOUTH_WEST], [SOUTH])

game.new_connection("Path To Playground",foodforest, playground, [WEST], [EAST])

game.new_connection("Brick Path", foodforest, office, [NORTH], [SOUTH])
 
game.new_connection("Stone Path", playground, office, [NORTH_EAST], [SOUTH_WEST])

game.new_connection("Path To Blacktop", playground, blacktop, [NORTH], [SOUTH])

game.new_connection("Woodchips", playground, porch, [WEST], [EAST])

game.new_connection("Stairs", office, supplyroom, [UP], [DOWN])

game.new_connection("Door To Room 5", porch, room5, [WEST], [EAST])

game.new_connection("Door To Room 6", porch, room6, [NORTH_WEST], [SOUTH_EAST])

game.new_connection("Door To Room 4", blacktop, room4, [EAST], [WEST])

game.new_connection("Computer Lab Door", blacktop, computerlab, [NORTH_EAST], [SOUTH_WEST])

game.new_connection("Door From Office", office, teacheroffice, [EAST], [WEST])

game.new_connection("Ramp", porch, barn, [NORTH], [SOUTH])

game.new_connection("Cement", blacktop, barn, [WEST], [EAST])

#willowwindforest/maze

game.new_connection("Forest Path", blacktop, forest1, [NORTH], [NOT_DIRECTION])

game.new_connection("Forest Path", forest1, forest2, [WEST], [EAST])

game.new_connection("Forest Path", forest1, forest3, [NORTH],[NOT_DIRECTION])

game.new_connection("Forest Path", forest1, forest4, [WEST],[EAST])                 

game.new_connection("Foest Path", forest2, shack, [NORTH_WEST], [SOUTH_WEST])

game.new_connection("Forest Path", forest2, forest3, [EAST,NORTH], [NOT_DIRECTION])

game.new_connection("Forest Path", forest4, forest3, [NORTH, WEST], [NORTH])

game.new_connection("Forest Path", forest3, creek, [NORTH_EAST], [SOUTH_WEST])

game.new_connection("Forest Path", forest2, blacktop, [SOUTH], [NOT_DIRECTION])

game.new_connection("Forest Path", forest1, forest1, [SOUTH], [SOUTH])

game.new_connection("Forest Path", forest2, forest2, [WEST], [WEST])

game.new_connection("Forest Path", forest4, forest4, [SOUTH], [SOUTH])

game.new_connection("Forest Path", forest4, forest4, [EAST], [EAST])


#WW game objets

asphalt = blacktop.new_object("asphalt chunk", "a chunk of asphalt broken from the blacktop")

key = barn.new_object("key", "a small brass key")

mathtest = room5.new_object("LA test", "an uncompleated LA test.")

sciencetest = room4.new_object("science test", "an uncompleated science test")

dullpencil = supplyroom.new_object("pencil", "an unsharpened pencil lying on the floor")

file_cabinet = room6.add_object(Container("File Cabinet","an old file cabinet"))

file_cabinet.new_object("math test",
                          """an uncompleated math test""")
file_cabinet.make_requirement(key)



#pencil sharpener
def sharpen_pencil(game,thing):
  thing.description = "a sharpened pencil"
  game.output("You sharpen the pencil. It is now ready to use.")
teacheroffice.add_phrase("sharpen pencil", sharpen_pencil, [dullpencil])

#test command
def do_math_test(game,thing):
  if  game.player.inventory["math test"].description == "a compleated math test":
    game.output("The test is already done.")
  else:
    if thing.description == "an unsharpened pencil lying on the floor":
      game.output("Your pencil is not sharp.")
    else:
      game.player.inventory["math test"].description = "a compleated math test"
      game.output("The test is now finished.")
  
dullpencil.add_phrase("do math test", do_math_test, [mathtest])
                        

def do_science_test(game,thing):
  if  game.player.inventory["science test"].description == "a compleated science test":
    game.output("The test is already done")
  else:
    if thing.description == "an unsharpened pencil lying on the floor":
      game.output("Your pencil is not sharp.")
    else:
      game.player.inventory["science test"].description = "a compleated science test"
      game.output("The test is now finished.")
  
dullpencil.add_phrase("do science test", do_science_test, [sciencetest])


def do_LA_test(game,thing):
  if  game.player.inventory["LA test"].description == "a compleated LA test":
    game.output("The test is already done")
  else:
    if thing.description == "an unsharpened pencil lying on the floor":
      game.output("Your pencil is not sharp.")
    else:
      game.player.inventory["science test"].description = "a compleated LA test"
      game.output("The test is now finished.")
  
dullpencil.add_phrase("do LA science", do_LA_test, [LAtest])

dullpencil.add_phrase("complete math test", do_math_test, [mathteset])

dullpencil.add_phrase("complete science test", do_science_test, [sciencetest])

dullpencil.add_phrase("complete LA test", do_LA_test, [LAtest])

dullpencil.add_phrase("fill out math test", do_math_test, [mathtest])

dullpencil.add_phrase("fill out science test", do_science_test, [sciencetest])

dullpencil.add_phrase("fill out LA test", do_LA_test, [LAtest])

#end of willow Wind     
#------------------     
#start of the MINE
centralmine = game.new_location(
"Central Mine",
"""You fall onto the ground and the portal shuts behind you. You get up and look around. You see exits in all four directions and an old rusty sword in a corner.""")

mineroom1 = game.new_location(
"Mine Room 1",
"""You are in a dirty, dimly lit mining room. There are exits to the East and Southwest.""")

mineroom2 = game.new_location(
"Mine Room 2",
"""You are in a dirty, dimly lit mining room with exits to the Northeast and Northwest""")

mineroom3 = game.new_location(
"mine Room 3",
"""You are in a dirty, dimly lit mining room. You see exits to the Northwest and Southwest.""")

nstunnel = game.new_location(
"North South Tunnel",
"""enter""")

mineroom4 = game.new_location(
"Mine Room 4",
"""A hungry troll looms over you. You see a pickaxe in the corner.""")

ewtunnel = game.new_location(
"East West Tunnel",
"""You are in dimly light a tunnel. There are exits to the East and West.""")

blockedroom = game.new_location(
"Blocked Room",
"""You see a blockade to the South of the room. There is an exit to the West.""")

cyclopsroom = game.new_location(
"Cyclops Room",
"""A giant cyclops looms over you with it's single giant eye. There are exits to the Southeast, South, and Southwest.""")

breakroom = game.new_location(
"Break Room",
"""You see some old wood chairs, and a table. There is an exit to the South""")

dimtunnel = game.new_location(
"Dim Tunnel",
"""You are in a dim tunnel. There are exits to the North, and South West.""")

keyroom = game.new_location(
"Key Room",
"""A key is glowing dimly on a pedestal.""")

storageroom4 = game.new_location(
"Storage Room",
"""There are mining supplies littered across the floor. There are exits to the North, North East, and South.""")

gemroom = game.new_location(
"Gem Room",
"""There is a green gem sticking out of the wall. There is an exit to the North.""")

mineshaftelevatorroom = game.new_location(
"Mineshaft Elavator Room",
"""There is an old elevator. You can go down, or out the exit to the North East.""")

generatorroom = game.new_location(
"Generator Room",
"""thair is large machrrinry infront of you and a large red button with a sighn that says /"atharized persons only"/""")

maintenanceroom = game.new_location(
"Maintace Room",
"""There is a broom in the corner. There are exits to the South and, North East.""")

goldroom = game.new_location(
"Gold Room", 
"""There is a pile of gold nuggets on the floor. There is an exit to the North.""")

minecartroom = game.new_location(
"Minecart Room",
"""There is a mine cart here not much to look at.""")

storageroom3 = game.new_location(
"Storage Room 3",
"""There are some supplies in the corner. There are exits to the South East, East, and North East.""")

mineshaft = game.new_location(
"Mine Shaft",
"""You are in a mine shaft, it's kind of dirty. There a exits to the South West, South East, East, and North.""")

smallroom = game.new_location(
"small Room",    
"""You are in a small room, there,s not much space to move around. There are exits to the West and, South East.""")

glowingroom = game.new_location(
"Glowing Room",
"""You are in a room where the walls seem to be glowing.""")

magiclanternroom = game.new_location(
"Magic Lantern Room",
"""A lantern lies in the corner of the room. There is an exit to the East.""")

darkroom = game.new_location(
"Dark Room",
"""""")

storageroom2 = game.new_location(
"Storage Room 2",
"""There are various supplies on the floor. There are exits to the East and, South.""")

damproom = game.new_location(
"Damp Room",
"""You are in a very humid room.""")

helmetroom = game.new_location(
"Helmet Room",
"""enter""")

widetunnel = game.new_location(
"Wide tunnel",  
"""enter""")

minekitchen = game.new_location(
"Mine kitchen",
"""enter""")

supplyroom = game.new_location(
"Supply Room",
"""enter""")

coatroom = game.new_location(
"Coat Room", 
"""enter""")

largeroom = game.new_location(
"Large Room",
"""enter""")

storageroom1 = game.new_location(
"Storage Room 1",
"""You are in a room that looks like it was holding something but not any more.""")

goblinroom = game.new_location(
"Goblin Room",
"""enter""")

coldroom = game.new_location(
"Cold Room",
"""You are in a cold room, there is an exit to the south.""")

mineexit = game.new_location(
"Mine Exit",
"""enter""")

ravinebridge = game.new_location(
"Ravine Bridge",
"""enter""")

#lowerminelocations
#----------------
 
lowerelevatormineshaft = game.new_location(
"lowerelevatormineshaft",
"""You are in an empty room, empty nothing nada zilch zero nutin.""")

emptyroom1 = game.new_location( 
"emptyroom",
"""Stil empty.""")

emptyroom2 = game.new_location(
"emptyroom",
"""Did you expect any thing other than nothing.""")

puddleroom = game.new_location(
"puddleroom",
"""There are some puddles here""")

batroom = game.new_location(
"giant bat room",
"""enter""")

narrowglowingpassage = game.new_location(
"narrowglowingpassage",
"""enter""")

emptyroom3 = game.new_location(
"emptyroom",
"""Even more empty.""")



#mine connections


game.new_connection("centralminetomineroom1", centralmine, mineroom1, [SOUTH],[NORTH]) 

game.new_connection("centralminetomineroom2", centralmine, mineroom2, [NORTH],[SOUTH])

game.new_connection("centralminetomineroom3", centralmine, mineroom3, [WEST],[EAST])

game.new_connection("centralminetomineroom4", centralmine, mineroom4, [EAST],[WEST])

game.new_connection("mineroom1toewtunnel", mineroom1, ewtunnel, [EAST], [WEST])

game.new_connection("ewtunneltoblockedroom", ewtunnel, blockedroom, [EAST], [WEST])

game.new_connection("blockedroomtocyclopsroom", blockedroom, cyclopsroom, [SOUTH], [NORTH])

game.new_connection("cyclopsroomtodimtunnel", cyclopsroom, dimtunnel, [SOUTH], [NORTH])

game.new_connection("cyclopsroomtobreakroom", cyclopsroom, breakroom, [WEST], [EAST])

game.new_connection("breakroomtostorageroom4", breakroom, storageroom4, [SOUTH], [NORTH])

game.new_connection("dimtunneltostorageroom4", dimtunnel, storageroom4, [SOUTH], [NORTH])

game.new_connection("storageroom4togemroom", storageroom4, gemroom, [SOUTH], [NORTH])

game.new_connection("cyclopsroomtokeyroom", cyclopsroom, keyroom, [SOUTH_EAST], [NORTH_WEST])

game.new_connection("mineroom1tomineshaftelavator", mineroom1, mineshaftelevatorroom, [SOUTH_WEST], [NORTH_EAST])

game.new_connection("elavatorroomtowarmroom", mineshaftelevatorroom, warm_or_cold_room, [SOUTH], [NORTH])

game.new_connection("loudroomtomaintenanceroom", loud_or_quite_room, maintenanceroom, [SOUTH_WEST], [NORTH_EAST])

game.new_connection("maintenanceroomtogoldroom", maintenanceroom, goldroom, [NORTH], [SOUTH])

game.new_connection("loudroomtonwtunnel", loud_or_quite_room, nstunnel, [SOUTH], [NORTH])

game.new_connection("nstunneltomineroom3", nstunnel, mineroom3, [EAST], [WEST])

game.new_connection("nstunneltostorageroom3", nstunnel, storageroom3, [NORTH_WEST], [SOUTH_EAST])

game.new_connection("storageroom3tominecartroom", storageroom3, minecartroom, [EAST], [WEST])

game.new_connection("mineroom3tominecartroom", mineroom3, minecartroom, [WEST], [EAST])

game.new_connection("storageroom3tomineshaft", storageroom3, mineshaft, [NORTH_EAST], [SOUTH_WEST])

game.new_connection("minecartroomtomineshaft", minecartroom, mineshaft, [NORTH_WEST], [SOUTH_EAST])

game.new_connection("mineshafttoravine", mineshaft, ravinebridge, [NORTH], [SOUTH])

game.new_connection("ravinetoglowingroom", ravinebridge, glowingroom, [NORTH_EAST], [SOUTH_WEST])

game.new_connection("glowingroomtomagiclanternroom", glowingroom, magiclanternroom, [WEST], [EAST])

game.new_connection("mineroom2tosmallroom", mineroom2, smallroom, [WEST], [EAST])

game.new_connection("mineroom2todarkroom2", mineroom2, darkroom, [NORTH_EAST], [SOUTH_WEST])

game.new_connection("darkroomtostorageroom2", darkroom, storageroom2, [NORTH], [SOUTH])

game.new_connection("storageroom2towidetunnle", storageroom2, widetunnel, [WEST], [EAST])

game.new_connection("widetunneltokitchen", widetunnel, minekitchen, [NORTH], [SOUTH])

game.new_connection("widetunneltostorageroom1", widetunnel, goblinroom, [EAST], [WEST])

game.new_connection("darkroomtodamproom", darkroom, damproom, [EAST], [WEST])

game.new_connection("damproomtohelmetroom", damproom, helmetroom, [SOUTH_EAST], [NORTH_WEST])

game.new_connection("helmetroomtosupplyroom", helmetroom, supplyroom, [EAST], [WEST])

game.new_connection("supplyroomtocoatroom", supplyroom, coatroom, [EAST], [WEST])

game.new_connection("supplyroomtolargeroom", supplyroom, largeroom, [NORTH], [SOUTH])

game.new_connection("storageroom2tofoblin", storageroom2, goblinroom, [SOUTH], [NORTH])

game.new_connection("largeroomtogoblinroom", largeroom, goblinroom, [NORTH_EAST], [SOUTH_WEST])

game.new_connection("goblinroomtocoldroom", goblinroom, coldroom, [EAST], [WEST])

game.new_connection("ccoldroomtomineexit", coldroom, mineexit, [SOUTH], [NORTH])


#lowermineconnections
#------------

game.new_connection("elavatorshafttoemtyroom", lowerelevatormineshaft, emptyroom1, [NORTH], [SOUTH])

game.new_connection("emptyroomtoemptyroom", emptyroom1, emptyroom2, [WEST], [EAST])

game.new_connection("lowerelevatormineshafttopuddleroom", lowerelevatormineshaft, puddleroom, [EAST], [WEST])

game.new_connection("puddleroomtobatroom", puddleroom, batroom, [SOUTH_EAST], [NORTH_WEST])

game.new_connection("batroomroomtonarowglowinpassage", batroom, narrowglowingpassage, [NORTH_EAST], [SOUTH_WEST])

game.new_connection("batroom", narrowglowingpassage, emptyroom3, [NORTH], [SOUTH])




#mine monsters
                    
goblin = Animal("goblin")
goblin.set_location(goblinroom)
goblin.set_allowed_locations([goblinroom])                    

crazyminer = Animal("crazy Miner")
crazyminer.set_location_(generatorroom)
crazyminer.set_allowed_locations([generatorroom])
                    
troll = Animal("troll")
crazyminer.set_location(trollroom)
crazyminer.set_allowed_locations([trollroom])
                    
cyclops = Animal("cyclops")
crazyminer.set_location(cyclopsroom)
crazyminer.set_allowed_locations([cyclopsroom])                   
             
giantbat = Animal("bat")
crazyminer.set_location(batroom)
crazyminer.set_allowed_locations([batroom])

#mine keys

pickaxekey = cyclopsroom.new_object("pick-axe", "the handle has splinters and the head looks very old and rusty")
cyclopsroom.make_requirement(pick_axekey)



#mine items


 




#mine genaroter
redbutton = false

def push_red_button(game.thing):
  if button_on:
    
    warm_or_cold_room = game.new_location(
"Warm room",
"""You are in a warm room.""")

 loud_or_quite_room = game.new_location(
"Loud room",
"""You are in a loud room.""")

    
    redbutton = true
    
else:
  
  warm_or_cold_room = game.new_location(
"Cold Room",
"""You are in a eri cold room""")

loud_or_quite_room = game.new_location(
"Quite room",
"""You are in a Quite room.""")

redbutton = false





  
  

  
  
#mine genreator room to warm/cold room (connection) and mine genreator room to loud/noise room (connection)
  
game.new_connection("warmroomtogeneratorroom", warm_or_cold_room, generatorroom, [SOUTH_WEST], [NORTH_EAST])

game.new_connection("generatorroomtoloudroom", generatorroom, loud_or_quite_room, [NORTH], [SOUTH])












player = game.new_player(topofdriveway)

game.run()
