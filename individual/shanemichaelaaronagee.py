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
  There is a door to the north.""")

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

key = office.new_object("key",
                        "this is a bronze small key")

linda_porch = game.new_location(
    "Small Blacktop Porch",
    "This is a small porch outside. Broken, crashed cars, all around the blacktop")

blacktop = game.new_location(
    "Blacktop Pathway"
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

game.new_connection("Robins door", three way fork, robins_room, [IN, NORTH], [OUT, SOUTH])

game.new_connection("Sues door", split_RLS, sues_room, [IN, WEST], [OUT, EAST])

game.new_connection("Lacys door", split_RLS, lacys_room, [IN, EAST], [OUT, WEST])

game.new_connection("Blacktop to RLS.", blacktop, split_RLS, [IN, NORTH], [OUT, SOUTH])

game.new_connection("Lindas porch door", lindas_room, linda_porch, [IN, WEST], [OUT, EAST])

game.new_connection("Storage2door", upstairs, storage_room2, [IN, WEST], [OUT, EAST])

game.new_connection("Storage1door", upstairs, storage_room1, [IN, EAST], [OUT, WEST])

andre = game.new_connection("Linda Lab", computer, lindas_room, [IN, SOUTH], [OUT, NORTH])

andre.make_requirement(key)

game.new_connection("Lab Door", step, computer, [IN, WEST], [OUT, EAST])

game.new_connection("Vestibule Door Outside", step, vestibule, [IN, NORTH], [OUT, SOUTH])

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


whiteboard_markedup = False

marker = Object("marker", "small red marker")

def draw_on_whiteboard(game,thing):
    global whiteboard_markedup
    whiteboard_markedup = True
    game.output("You write on the board without thinking, it seems you wrote some sort of spell. !ERAD TI!")

marker.add_phrase(["draw on whiteboard", "draw on board"], draw_on_whiteboard)



lindas_room.add_object(marker)

def read_board(game,thing):
    global whiteboard_markedup
    if whiteboard_markedup:
        morokunda = Actor("Huge Three Headed Monster.")
        morokunda.set_location(thing)
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
                   "you kill the zombie.")

miniz = Actor("tiny zombie")
miniz.set_location(family)
game.add_actor(miniz)
shield = vestibule.new_object("shield", "a shiny pair of armor")
knife = office.new_object("knife", "a rusty old knife")
def fight_miniz(game, thing):
    if not "shield" in game.player.inventory:
        game.output("You try to stab the zombie with the knife, but it bites you.")

        game.output("You turn to the undead.")
    
        player.terminate()
    else:
        game.output("Using the shield to avoid the dragon's flames you kill it with the sword.")

        miniz.terminate()

miniz.add_phrase("fight zombie", fight_miniz)

def fight_morokunda(game, thing):
    if not "ninja_sword" in game.player.inventory:
        game.output("You try to stab the zombie with the ninja sword, but it bites you.")

        game.output("You have died.")
    
        player.terminate()
    else:
        game.output("Using the ninja sword to avoid it's giant tenticles, and stab the giant beast.")

        morokunda.terminate()

morokunda.add_phrase("fight monster", fight_morokunda)

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
