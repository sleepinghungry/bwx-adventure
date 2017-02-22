import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from bwx_adventure.advent import *
from bwx_adventure.advent import Game, Location, Connection, Object, Animal, Robot, Pet, Player
from bwx_adventure.advent import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION


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
"""You are in the schools garden. Th ere are garden beds all around and a pile of compost against one fence. There is a feild to the south.""")

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
"""You are in the computer lab of the school. There are computers on tables all around the room. The blacktop is to the southwest.""")

room5 = game.new_location(
"Room 5",
"""You are in room 5. One of the schools classrooms. There are tables all around the room and a sofa in the back. On one of the tables is an uncompleted LA test. The porch is to east.""")

room6 = game.new_location(
"Room 6",
"""You are in room 6. One of the school's classrooms. There are tables and a few desks around the room. On the side of the room is a large green sheet of fabric suspended on a frame. It appears to be a greenscreen. Against the wall is an old file cabinet. The porch is to the southeast.""")

porch = game.new_location(
"Porch",
"""You are on a porch in front of two classrooms. Room 5 is to the west, and room 6 is to the northwest.""")

barn = game.new_location(
"Barn",
"""You are inside the large red barn. It has been converted into what looks like a space for dancing. In the corner of the room is a drinking fountain and a closet. The porch is to the south and the blacktop is to the east.""")

teacheroffice = game.new_location(
  "Teacher's Office",
  """You are in a room in which each of the teachers have a desk. There is a bathroom in the corner and a pencil sharpener on the wall. The office is to the east.""")
supplyroom = game.new_location(
  "Supply Room",
  """You are in an upstairs supply room. There are boxes os school supplies around the edge of the room. The only exit is down the way you came from.""")

inportal = game.new_location(
  "Portal",
  """You are hovering in a swerling vortex of color. Direction and time are meaningless. You fell youself drifting through a trace like state. Ahead of you appears a black doorway and behind you a white one.""")

whitedeath = game.new_location(
  "Death",
  """You pass through the white door and suddenly feel your body fractured into miniscule particals. You are dead.""")

centralmine = game.new_location(
"Central Mine",
"""You are in a dimly lit dusty room. It appears to be a room in a long abbandoned mine. There are exits in all four directions.""") 

#WW game connections
game.new_connection("Driveway", topofdriveway, parkinglot, [NORTH], [SOUTH])

game.new_connection("Path To Field", topofdriveway, field, [WEST], [EAST])

game.new_connection("Path To Garden", field, garden, [NORTH], [SOUTH])

game.new_connection("Gravel Walkway", parkinglot, playground, [NORTH], [SOUTH])

game.new_connection("Food Forest Gate", parkinglot, foodforest, [NORTH_EAST], [SOUTH, SOUTHWEST])

game.new_connection("Path To Playground",foodforest, playground, [WEST], [EAST])

game.new_connection("Brick Path", foodforest, office, [NORTH], [SOUTH])
 
game.new_connection("Stone Path", playground, office, [NORTH_EAST], [SOUTH_WEST])

game.new_connection("Path To Blacktop", playground, blacktop, [NORTH], [SOUTH])

game.new_connection("Woodchips", playground, porch, [WEST], [EAST])

game.new_connection("Stairs", office, supplyroom, [UP], [DOWN])

game.new_connection("Door To Room 5", porch, room5, [WEST], [EAST])

game.new_connection("Door To Room 6", porch, room6, [NORTH_WEST], [SOUTH_EAST, EAST])

game.new_connection("Door To Room 4", blacktop, room4, [EAST], [WEST])

game.new_connection("Computer Lab Door", blacktop, computerlab, [NORTH_EAST], [SOUTH_WEST, SOUTH])

game.new_connection("Door From Office", office, teacheroffice, [EAST], [WEST])

game.new_connection("Ramp", porch, barn, [NORTH], [SOUTH])

game.new_connection("Cement", blacktop, barn, [WEST], [EAST])

game.new_connection("White Door", inportal, whitedeath, [OUT], [NOT_DIRECTION])

game.new_connection("Black door", inportal, centralmine, [IN], [NOT_DIRECTION])


#willowwindforest/maze
shack = game.new_location(
"Shack",
"""You're in a shack. There is not much light but you can make out a small machene in the middle of the room. It looks like it is a test grading machene.""")

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

game.new_connection("Forest Path", blacktop, forest1, [NORTH], [NOT_DIRECTION])

game.new_connection("Forest Path", forest1, forest2, [WEST], [EAST])

game.new_connection("Forest Path", forest1, forest3, [NORTH], [NOT_DIRECTION])

game.new_connection("Forest Path", forest1, forest4, [EAST], [WEST])                 

game.new_connection("Foest Path", forest2, shack, [NORTH_WEST], [SOUTH_EAST, SOUTH])

game.new_connection("Forest Path", forest2, forest3, [NORTH], [NOT_DIRECTION])

game.new_connection("Forest Path", forest4, forest3, [NORTH], [NORTH])

game.new_connection("Forest Path", forest3, creek, [NORTH_EAST], [SOUTH, SOUTH_WEST])

game.new_connection("Forest Path", forest2, blacktop, [SOUTH], [NOT_DIRECTION])

game.new_connection("Forest Path", forest1, forest1, [SOUTH], [SOUTH])

game.new_connection("Forest Path", forest2, forest2, [WEST], [WEST])

game.new_connection("Forest Path", forest4, forest4, [SOUTH], [SOUTH])

game.new_connection("Forest Path", forest4, forest4, [EAST], [EAST])

game.new_connection("Forest Path", forest3, forest3, [SOUTH], [SOUTH])

#WW game objets

asphalt = blacktop.new_object("asphalt chunk", "a chunk of asphalt broken from blacktop")

key = barn.new_object("key", "a small brass key")

LAtest = room5.new_object("LA test", "an uncompleted LA test.")

sciencetest = room4.new_object("science test", "an uncompleted science test")

dullpencil = supplyroom.new_object("pencil", "an unsharpened pencil lying on the floor")

file_cabinet = room6.add_object(Container("file cabinet","an old file cabinet"))

mathtest = file_cabinet.new_object("math test",
 """an uncompleted math test""")
file_cabinet.make_requirement(key)







#pencil sharpener
def sharpen_pencil(game,thing):
  thing.description = "a sharpened pencil"
  game.output("You sharpen the pencil. It is now ready to use.")
dullpencil.add_phrase("sharpen pencil", sharpen_pencil, [teacheroffice])

#test command
def do_math_test(game,thing):
  if  game.player.inventory["math test"].description == "a completed math test":
    game.output("The test is already done.")
  else:
    if thing.description == "an unsharpened pencil lying on the floor":
      game.output("Your pencil is not sharp.")
    else:
      game.player.inventory["math test"].description = "a completed math test"
      game.output("The test is now finished.")
  
dullpencil.add_phrase("do math test", do_math_test, [mathtest])
                        

def do_science_test(game,thing):
  if  game.player.inventory["science test"].description == "a completed science test":
    game.output("The test is already done")
  else:
    if thing.description == "an unsharpened pencil lying on the floor":
      game.output("Your pencil is not sharp.")
    else:
      game.player.inventory["science test"].description = "a completed science test"
      game.output("The test is now finished.")
  
dullpencil.add_phrase("do science test", do_science_test, [sciencetest])


def do_LA_test(game,thing):
  if  game.player.inventory["LA test"].description == "a completed LA test":
    game.output("The test is already done")
  else:
    if thing.description == "an unsharpened pencil lying on the floor":
      game.output("Your pencil is not sharp.")
    else:
      game.player.inventory["LA test"].description = "a completed LA test"
      game.output("The test is now finished.")
  
dullpencil.add_phrase("do LA test", do_LA_test, [LAtest])

dullpencil.add_phrase("complete math test", do_math_test, [mathtest])

dullpencil.add_phrase("complete science test", do_science_test, [sciencetest])

dullpencil.add_phrase("complete LA test", do_LA_test, [LAtest])

dullpencil.add_phrase("fill out math test", do_math_test, [mathtest])

dullpencil.add_phrase("fill out science test", do_science_test, [sciencetest])

dullpencil.add_phrase("fill out LA test", do_LA_test, [LAtest])


#test grading machine
test_counter = 0
def grade_math_test(game, thing):
  if game.player.inventory["math test"].description == "a completed math test":
    game.output ("Good job you aced the test 100%!")
    del(game.player.inventory["math test"])
    global test_counter
    test_counter += 1
  else:
    game.output ("The grading machine spits out the test. It is not completed.")

mathtest.add_phrase("grade math test", grade_math_test, [shack])
mathtest.add_phrase("put math test in machine", grade_math_test, [shack])



def grade_LA_test(game, thing):
  if game.player.inventory["LA test"].description == "a completed LA test":
    game.output ("Good job you aced the test 100%!")
    del(game.player.inventory["LA test"])
    global test_counter
    test_counter += 1
  else:
    game.output ("The grading machine spits out the test. It is not completed.")

LAtest.add_phrase("grade LA test", grade_LA_test, [shack])
LAtest.add_phrase("put LA test in machine", grade_LA_test, [shack])


def grade_science_test(game, thing):
  if game.player.inventory["science test"].description == "a completed science test":
    game.output ("Good job you aced the test 100%!")
    del(game.player.inventory["science test"])
    global test_counter
    test_counter += 1
  else:
    game.output ("The grading machine spits out the test. It is not completed.")

sciencetest.add_phrase("grade science test", grade_science_test, [shack])
sciencetest.add_phrase("put math test in machine", grade_science_test, [shack])


def open_portal(game, thing):
  game.new_connection("portal", shack, inportal, [NORTH], [NOT_DIRECTION],)


if test_counter == 3:
  open_portal
  game.output("The grading machine makes a soft clicking sound and a swirling blue and purple portal appears at the north end of the shack. You feel a slight breeze pull your hair toward it.")







player = game.new_player(topofdriveway)

game.run()
