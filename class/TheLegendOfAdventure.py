
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

player = game.new_player (topofdriveway)



#Willowwind game part

<<<<<<< HEAD
topofdriveway = game.new_location(
  "Top Of Driveway",
=======
driveway = game.new_location(
  "Driveway",
>>>>>>> origin/master
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
"""You are in room 6. One of the school's classrooms. There are tables and a few desks around the room. On the side of the room is a large green sheet of fabric suspended on a frame. It appears to be a greenscreen. The porch is to the southeast.""")

barn = game.new_location(
"Barn",
"""You are inside the large red barn. It has been converted into what looks like a space for dancing. In the corner of the room is a drinking fountain and a closet. The porch is to the south and the blacktop is to the east.""")

shack = game.new_location(
"Shack",
"""You're in a shack. There is not much light but you can make out a small machene in the middle of the room. It looks like it is a test grading machene.""")

porch = game.new_location(
"Porch",
"""You are on a porch in front of two classrooms. Room 5 is to the east, and room 6 is to the northeast.""")
 
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
  "Teacher's Office"
  """You are in a room in which each of the teachers have a desk. There is a bathroom in the corner and a pencil sharpener on the wall. The office is to the east."""

#WW game connections
game.new_connection("Driveway", topofdriveway, parkinglot, [NORTH], [SOUTH])

game.new_connection("Path To Field", topofdriveway, field, [WEST], [EAST])

game.new_connection("Path To Garden", field, garden, [NORTH], [SOUTH])

game.new_connection("Gravel Walkway", parkinglot, playground, [NORTH], [SOUTH])

game.new_connection("Food Forest Gate", parkinglot, foodforest, [NORTH_EAST] [SOUTH_WEST,SOUTH])

game.new_connection("Path To Playground",foodforest, playground, [WEST], [EAST])

game.new_connection("Brick Path", foodforest, office, [NORTH], [SOUTH])
 
game.new_connection("Stone Path", playground, office, [NORTH_EAST], [SOUTH_WEST])

game.new_connection("Path To Blacktop", playground, blacktop, [NORTH], [SOUTH])

game.new_connection("Woodchips", playground, porch, [WEST], [EAST])

game.new_connection("Stairs", office, supplyroom, [UP], [DOWN])

game.new_connection("Door To Room 5", porch, room5, [EAST], [WEST])

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

game.new_connection("Forest Path", forest2, blacktop, [SOUTH], [NOT_DIRECTION]

#WW game objets

asphalt = blacktop.new_object("Asphalt Chunk", "a chunk of asphalt broken from the blacktop")

mathtest = room5.new_object("LA Test", "an uncompleated LA test.")

sciencetest = room4.new_object("Science Test", "an uncompleated science test")

dullpencil = supplyroom.new_object("Unsharpened Pencil", "an unsharpened pencil lying on the floor")

#pencil sharpener
def sharpen_pencil(game,thing):
  thing.name = "Sharpened Pencil"
  thing.description = ""
  
teacheroffice.add_phrase("sharpen pencil", sharpen_pencil, dullpencil)
#teacheroffice.add_phrase("sharpen pencil", sharpen_pencil, [dullpencil])




                        
#end of willow Wind     
#------------------     
#start of the MINE

central mine = game.new_location(
"Central Mine",
"""You fall onto the ground and the portal shuts behind you. You get up and look around. You see exits in all four directions and an old rusty sword in a corner.""")


mineroom1 = game.new_location(
"Mine Room 1",
"""You are in a dirty, dimly lit mining room. There are exits to the East and Southwest.""")


mineroom2 = game.new_location(
"Mine Room 2"
"""You are in a dirty, dimly lit mining room with exits to the Northeast and Northwest""")

mineroom3 = game.new_location(
"mine Room 3"
"""You are in a dirty, dimly lit mining room. You see exits to the Northwest and Southwest.""")

mineroom4 = game.new_location(
"Mine Room 4"
"""A hungry troll looms over you. You see a pickaxe in the corner.""")

ewTunnel = game.new_location(
"East West Tunnel"
"""You are in a tunnel. There are exits to the East and West.""")

blockedroom = game.new_location(
"Blocked Room"
"""""")

cyclopsroom = game.new_location(
"Cyclops Room
"""enter""")

breakroom = game.new_location(
"Break Room"
"""enter""")

dimtunnel = game.new_location(
"Dim Tunnel"
"""enter""")

keyroom = game.new_location(
"Key Room"
"""There is a dimly glowing key siting on a pedestal.""")

storageroom4 = game.new_location(
"Storage Room"
"""enter""")

gemroom = game.new_location(
"Gem Room"
"""enter""")

mineshaftelevatorroom = game.new_location(
"Mineshaft Elavator Room" 
"""enter""")

warmroom = game.new_location(
"Warm room"
"""""")

generatorroom = game.new_location(
"Generator Room"
"""enter""")

loudroom = game.new_location(
"Loud room"
"""enter""")

maintenanceroom = game.new_location(
"Maintace Room"
"""enter""")

goldroom = game.new_location(
"Gold Room" 
"""enter""")

minecartroom = game.new_location(
"Minecart Room"
"""enter""")

storageroom3 = game.new_location(
"Storage Room 3"
"""""")

mineshaft = game.new_location(
"Mine Shaft"
"""enter""")

smallroom = game.new_location(
"small Room"    
"""enter""")

glowingroom = game.new_location(
"Glowing Room"
"""enter""")

magiclanternroom = game.new_location(
"Magic Lantern Room"
"""enter""")

darkroom = game.new_location(
"Dark Room"
"""enter""")

storageroom2 = game.new_location(
"Storage Room 2"
"""enter""")

damproom = game.new_location(
"Damp Room"
"""enter""")

helmetroom = game.new_location(
"Helmet Room"
"""enter""")

widetunnel = game.new_location(
"Wide tunnel" 
"""enter""")

minekitchen = game.new_location(
"Mine kitchen"
"""enter""")

supplyroom = game.new_location(
"Supply Room"
"""enter""")

coatroom = game.new_location(
"Coat Room" 
"""enter""")

largeroom = game.new_location(
"Large Room"
"""enter""")

storageroom1 = game.new_location(
"Storage Room 1
"""enter""")

goblinroom = game.new_location(
"Goblin Room"
"""enter""")

coldroom = game.new_location(
"Cold Room"
"""enter""")

mineexit = game.new_location(
"Mine Exit"
"""enter""")

#lowerminelocations
#----------------
 
lowerelavatormineshaft = game.new_location( 

emptyroom1 = game.new_location( 
"emptyroom"
"""enter""")

emptyroom2 = game.new_location(
"emptyroom"
"""enter""")

puddleroom = game.new_location(
"puddleroom"
"""enter""")

batroom = game.new_location(
"giant bat room"
"""enter""")

narrowglowingpassage = game.new_location(
"narrowglowingpassage"
"""enter""")

emptyroom3 = game.new_location(
"emptyroom"
"""enter""")



#mine connections


game.new_connection("centralminetomineroom1", centralmine, mineroom1, [SOUTH],[NORTH]) 

game.new_connection("centralminetomineroom2", centralmine, mineroom2, [NORTH],[SOUTH])

game.new_connection("centralminetomineroom3", centralmine, mineroom3, [WEST],[EAST])

game.new_connection("centralminetomineroom4", centralmine, mineroom4, [EAST],[WEST])

game.new_connection("mineroom1toewtunnel", mineroom1, ewtunnel, [EAST], [WEST])

game.new_connection("ewtunneltoblockedroom", ewtunnel, blockedroom, [EAST], [WEST])

game.new_connection("blockedroomtocyclopsroom", blockedroom, cyclopseroom, [SOUTH], [NORTH])

game.new_connection("cyclopsroomtodimtunnel", cyclopseroom, dimtunnel, [SOUTH], [NORTH])

game.new_connection("cyclopsroomtobreakroom", cyclopseroom, breakroom, [WEST], [EAST])

game.new_connection("breakroomtostorageroom4", breakroom, storageroom4, [SOUTH], [NORTH])

game.new_connection("dimtunneltostorageroom4", dimtunnel, storageroom4, [SOUTH], [NORTH])

game.new_connection("storageroom4togemroom", storageroom4, gemroom, [SOUTH], [NORTH])

game.new_connection("cyclopsroomtokeyroom", cyclopseroom, keyroom, [SOUTH_EAST], [NORTH_WEST])

game.new_connection("mineroom1tomineshaftelavator", mineroom1, mineshaftelavatorroom, [SOUTH_WEST], [NORTH_EAST])

game.new_connection("elavatorroomtowarmroom", mineshaftelavatorroom, warmroom, [SOUTH], [NORTH])

game.new_connection("warmroomtogeneratorroom", warmroom, generatorroom, [SOUTH_WEST], [NORTH_EAST])

game.new_connection("generatorroomtoloudroom", generatorroom, loudroom, [NORTH], [SOUTH])

game.new_connection("loudroomtomantaceroom", loudroom, matenaceroom, [SOUTH_WEST], [NORTH_EAST])

game.new_connection("matenaceroomtogoldroom", matenaceroom, goldroom, [NORTH], [SOUTH])

game.new_connection("loudroomtonwtunnel", loudroom, nstunnel, [SOUTH], [NORTH])

game.new_connection("nstunneltomineroom3", nstunnel, mineroom3, [EAST], [WEST])

game.new_connection("nstunneltostorageroom3", nstunnel, storageroom3, [NORTH_WEST], [SOUTH_EAST])

game.new_connection("storageroom3tominecartroom", storageroom3, minecartroom, [EAST], [WEST])

game.new_connection("mineroom3tominecartroom", mineroom3, minecartroom, [WEST], [EAST])

game.new_connection("storageroom3tomineshaft", storageroom3, mineshaft, [NORTH_EAST], [SOUTH_WEST])

game.new_connection("minecartroomtomineshaft", minecartroom, mineshaft, [NORTH_WEST], [SOUTH_EAST])

game.new_connection("mineshafttoravine", mineshaft, ravinebridge, [NORTH], [SOUTH])

game.new_connection("ravinetoglowingroom", ravinebridge, glowingroom, [NORTH_EAST], [SOUTH_WEST])

game.new_connection("glowingroomtomagiclantrenroom", glowingroom, magiclantrenroom, [WEST], [EAST])

game.new_connection("mineroom2tosmallroom", mineroom2, smallroom, [WEST], [EAST])

game.new_connection("mineroom2todarkroom2", mineroom2, darkroom, [NORTH_EAST], [SOUTH_WEST])

game.new_connection("darkroomtostorageroom2", darkroom, storageroom2, [NORTH], [SOUTH])

game.new_connection("storageroom2towidetunnle", storageroom2, widetunnel, [WEST], [EAST])

game.new_connection("widetunneltokitchen", widetunnel, minekitchen, [NORTH], [SOUTH])

game.new_connection("widetunneltostorageroom1", widetunnel, goblinroom, [EAST], [WEST])

game.new_connection("darkroomtodamproom", darkroom, damproom, [EAST], [WEST])

game.new_connection("damproomtohelmetroom", damproom, helmetroom, [SOUTH_EAST], [NORTH_WEST])

game.new_connection("helmetroomtosupplyroom", helmetroom, supply, [EAST], [WEST])

game.new_connection("supplyroomtocoatroom", supplyroom, coatroom, [EAST], [WEST])

game.new_connection("supplyroomtolargeroom", supplyroom, largeroom, [NORTH], [SOUTH]

game.new_connection("storageroom2tofoblin", storageroom2, goblinroom, [SOUTH], [NORTH])

game.new_connection("largeroomtogoblinroom", largeroom, goblinroom, [NORTH_EAST], [SOUTH_WEST])

game.new_connection("goblinroomtocoldroom", goblinroom, coldroom, [EAST], [WEST])

game.new_connection("ccoldroomtomineexit", coldroom, mineexit, [SOUTH], [NORTH])

#lowermineconnections
#------------

game.new_connection("elavatorshafttoemtyroom", lowerelavatormineshaft, emptyroom1, [NORTH], [SOUTH])

game.new_connection("emptyroomtoemptyroom", emptyroom, emptyroom, [WEST], [EAST])

game.new_connection("lowerelavatorroomtopuddleroom", lowerelavtorroom, puddleroom, [EAST], [WEST])

game.new_connection("puddleroomtominntorroom", puddleroom, minnatarroom, [SOUTH_EAST], [NORTH_WEST])

game.new_connection("minnatarroomtonarowglowinpassage", minnatarroom, narrowglowingpassage, [NORTH_EAST], [SOUTH_WEST])

game.new_connection("batroom", narrowglowingpassage, magicshelidroom, [NORTH], [SOUTH])




#mine monsters
                    
goblin = Animal("goblin")
  enemy.set_location(goblinroom)
  enemy.set_allowed_locations([goblinroom])                    

crazyminer = Animal("crazy Miner")
  enemy.setlocation_(genoratorroom)
  enemy.set_allowed_locations([genoratorroom])
                    
troll = Animal("troll")
  enemy.set_location(trollroom)
  enemy.set_allowed_locations([trollroom])
                    
cyclops = Animal("cyclops")
 enemy.set_location(cyclopsroom)
 enemy.set_allowed_locations([cyclopsroom])                   
             
giantbat = Animal("bat")
  enemy.set_location(batroom)
  enemy.set_allowed_locations([batroom])

#mine keys

pickaxekey = cyclopsroom.new_object("pick-axe", "the handle has splinters and the head looks very old and rusty")
cyclopsroom.make_requirement(pick_axekey)



#mine items

                   





#mine genaroter














player = game.new_player(driveway)

game.run()
