import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
sys.path.insert(1, os.path.join(sys.path[0], '../bwx_adventure'))
from bwx_adventure.advent import *
from bwx_adventure.advent_devtools import *

game = Game("Willow Of Death")

porch = game.new_location(
  "Porch",
  "You are on a porch. It is raining. To the North is an office door to the west is a ramp.")

player = game.new_player(porch)

vestibule = game.new_location(
  "Vestibule",
  "This is a small area at the bottom of a flight of stairs. There is an office door to the west. You have an exit from where you came.")

upstairs = game.new_location(
    "Upstairs Hallway",
    "This is a hallway with a door to the east, And stairs going down.")

office = game.new_location(
  "Office",
  """A nicely organized office.
  There is a door to the east.""")

family = game.new_location(
  "Family Room",
  "This is a large room with a fridge and an open window to the north. There is also a door to the west.")

yard = game.new_location(
  "Yard",
  "This is a small yard with barbed wire all around. There is only an exit from were you came.")

step = game.new_location(
  "Stepway",
  "This is a stepway with a door to the north and west.")

computer = game.new_location(
  "Computer Lab",
  "This is a small room with tables spread out in the room.")

lindas_room = game.new_location(
  "Room Four",
  "This is a skinny but tall room. There is a whitebourd here.")

storage_room1 = game.new_location(
  "Storage Room 1",
  "This is a large room with boxes of school suplies.")

storage_room2 = game.new_location(
    "Storage Room 2",
    "More boxes and more boxes...")

key = office.new_object(
    "key",
    "this is a bronze small key")

linda_porch = game.new_location(
    "Small Blacktop Porch",
    "This is a small porch outside. Broken, crashed cars, all around the blacktop")

blacktop = game.new_location(
    "Blacktop Pathway",
    "There is one small pathway to a room leading North.")

split_RLS = game.new_location(
    "Three way fork",
    "There are three rooms here. One to the West saying SUE, another to the North saying ROBIN, and the final to the East saying LACY.")

robins_room = game.new_location(
    "Robins room",
    "This is an all around large room, with a nice opening to the East.")

sues_room = game.new_location(
    "Sues room",
    "A small well organized room.")

lacys_room = game.new_location(
    "Lacys room",
    "It's to dark to see anything in here.")

secretrd = game.new_location(
    "Robins room prt2",
    "This is a very tight space, with tons of book shelfs. There is a trap door under a wooden chair.")

mazelol = game.new_location(
    "Maze room one LOL",
    "This is a room going in four different directions no ends to be seen.")

secret_maze = game.new_location(
    "Secret Room In Maze",
    "This is a room with very nice decorations.")

apple_sword = secret_maze.new_object(
    "ninja sword",
    "ancient ninja sword")

bathroom1 = game.new_location(
    "Bathroom 1",
    "Small bathroom with a toilet and a sink.")

cellar_passage = game.new_location(
     "Cellar Passage",
     "This is a dark cold hallway that leeds north.")

cellar_passage1 = game.new_location(
     "Cellar Passage",
     "small empty corner room with passage west, and from where you came.")

cellar_passage2 = game.new_location(
     "Cellar Passage",
     "cold empty hallway leading west.")

cellar_barn = game.new_location(
     "Cellar Passage",
     "This is a small area with a ladder leading to a trap door.")

barn = game.new_location(
     "Barn",
     "This is a lardge barn with a stage to the north, and a door to the south.")

bkey = lacys_room.new_object(
     "Key",
     "Small barn shaped key.")

#stage = game.new_location(
#     "Stage",
#     "Large stage with wordrobe.")
open_fridge = False

def open_fridge(game,thing):
     global family
     open_fridge = True
     print("The fridge is open revealing a botle of Dr.Pepper on the bottom shelf.")
family.add_phrase("open fridge", open_fridge)

pull_soda = False

def pull_soda(game,thing):
     global family
     global cellar_passage
     pull_soda = True
     print("The Dr.Pepper was a lever and you pulled it. A secret passage has apeared from inside the fridge.")
     game.new_connection("Secret Fridge Passage", family, cellar_passage, [IN, EAST], [OUT, WEST])
family.add_phrase(["take soda", "take dr.pepper", "take Dr.Pepper"], pull_soda)

def move_chair(game, thing):
     global secretrd 
     global mazelol
     game.new_connection("Trap door RR", secretrd, mazelol, [IN, DOWN], [OUT, UP])
     game.output("The chair has been moved.")
secretrd.add_phrase(["move chair", "pull chair"], move_chair)

game.player.health = 30

araya = game.new_connection("Trap Barn Door", cellar_barn, barn, [IN, UP], [OUT, DOWN])

araya.make_requirement(bkey)

game.new_connection("Cellar to Cellar Barn", cellar_passage2, cellar_barn, [IN, WEST], [OUT, EAST])

game.new_connection("Secret Cellar1", cellar_passage1, cellar_passage2, [IN, WEST], [OUT, EAST])

game.new_connection("Secret Sellar", cellar_passage, cellar_passage1, [IN,NORTH], [OUT, SOUTH])

game.new_connection("Bathroom Door", family, bathroom1, [IN, WEST], [OUT, EAST])

game.new_connection("Secret lol", mazelol, secret_maze, [IN, DOWN], [OUT, UP])

game.new_connection("secret robin", robins_room, secretrd, [IN, EAST], [OUT, WEST])

game.new_connection("Porch Top", linda_porch, blacktop, [IN, NORTH], [OUT, SOUTH])

game.new_connection("Robins door", split_RLS, robins_room, [IN, NORTH], [OUT, SOUTH])

game.new_connection("Sues door", split_RLS, sues_room, [IN, WEST], [OUT, EAST])

game.new_connection("Lacys door", split_RLS, lacys_room, [IN, EAST], [OUT, WEST])

game.new_connection("Blacktop to RLS.", blacktop, split_RLS, [IN, NORTH], [OUT, SOUTH])

game.new_connection("Lindas porch door", lindas_room, linda_porch, [IN, WEST], [OUT, EAST])

game.new_connection("Storage2door", upstairs, storage_room2, [IN, WEST], [OUT, EAST])

game.new_connection("Storage1door", upstairs, storage_room1, [IN, EAST], [OUT, WEST])

andre = game.new_connection("Linda Lab", computer, lindas_room, [IN, SOUTH], [OUT, NORTH])

andre.make_requirement(key)

game.new_connection("Lab Door", step, computer, [IN, WEST], [OUT, EAST])

game.new_connection("Vestibule Door Outside", step, family, [IN, NORTH], [OUT, SOUTH])

game.new_connection("Ramp", porch, step, [IN, WEST], [OUT, EAST])

game.new_connection("Window", family, yard, [IN, NORTH], [OUT, SOUTH])

game.new_connection("Stairs", vestibule, upstairs, [IN, UP], [OUT, DOWN])

game.new_connection("Vestibule Door", porch, vestibule, [IN, NORTH], [OUT, SOUTH])

game.new_connection("Office Door", vestibule, office, [IN, WEST], [OUT, EAST])

dog = Pet("Dog")
dog.set_location(porch)
dog.set_allowed_locations([porch])

yard.add_object(Drink("vial",
                          "a small vial of bright green glowing liquid",
                          Die("choking violently and collapsing onto the floor..."),
                          Object("empty vial", "an empty vial with an acrid odor")))

bathroom1.new_object("pile of toilet paper",
                         "soggy pile of toilet paper on floor.")

whiteboard_markedup = False

marker = Object("marker", "small red marker")

def draw_on_whiteboard(game,thing):
    global whiteboard_markedup
    whiteboard_markedup = True
    game.output("You write on the board without thinking, it seems you wrote some sort of spell. !ERAD TI!")

marker.add_phrase(["draw on whiteboard", "draw on board"], draw_on_whiteboard)

storage_room1.add_object(marker)

armor = vestibule.new_object("armor", "a shiny pair of armor")

def put_on_armor(game,thing):
    game.player.health += 20
    game.output("You put the armor and become more protected.")
armor.add_phrase(["wear armor", "put on armor", "equip armor"], put_on_armor)



morokunda = None

def read_board(game,thing):
    global whiteboard_markedup
    global morokunda
    if whiteboard_markedup:
        morokunda = Actor("Huge Three Headed Monster.")
        morokunda.set_location(thing)
        morokunda.add_phrase("fight monster", fight_morokunda)
        game.add_actor(morokunda)
        game.output("A giant 3 headed monster has appeared in the room!")
    else:
        game.output("There is nothing to read.")
lindas_room.add_phrase(["read board", "read whiteboard"], read_board)


zombie = Animal("zombie")
zombie.set_location(yard)
zombie.set_allowed_locations([yard])
game.add_actor(zombie)
zombie.add_phrase("fight zombie",
                   Say("you kill the zombie with a massive stab through the heart."))

miniz = Actor("tiny zombie")
miniz.set_location(family)
game.add_actor(miniz)
knife = office.new_object("knife", "a rusty old knife")
def fight_miniz(game, thing):
    if not "knife" in game.player.inventory:
        game.output("You try to stab the zombie with the knife, but it bites you.")

        game.output("You turn to the undead.")
    
        player.terminate()
    else:
        game.output("You stab the zombie and as you do he shreeks and dies.")

        miniz.terminate()

miniz.add_phrase("fight tiny zombie", fight_miniz)

def fight_morokunda(game, thing):
    if "ninja sword" in game.player.inventory:
        game.output("Using the ninja sword to avoid it's giant tenticles, and stab the giant beast.")

        morokunda.terminate()

    else:
        game.output("You have nothing strong enouph to peirce it's skin.")

        game.output("You have died.")
    
        player.terminate()

game.add_actor(player)
game.add_actor(dog)
test_script = Script("test",
"""
> look
> take vial
> give dog vial
> tell dog drink vial
> look
> end
""")

player.add_script(test_script)

game.run()
