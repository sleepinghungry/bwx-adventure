import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
sys.path.insert(1, os.path.join(sys.path[0], '../../bwx_adventure'))
from bwx_adventure.advent import *
from bwx_adventure.advent_devtools import *

game = Game("Willow Of Death")

playername = input("GUARDIAN ANGEL: What is your name???")
print("GUARDIAN ANGEL: Well", playername, "it's nice to see someone is alive, you are one of few survivers of the zombie apacolypse."
      " But you are blind, don't worry I am your guardian angel, I will explain everything as you go... good luck...")

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
  "This is a small room with tables spread out in the room, and a door to the south.")

lindas_room = game.new_location(
  "Room Four",
  "This is a skinny but tall room. There is a whitebourd here, and a door to the west.")

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

bkey = Object("skull key", "Small barn shaped key.")

stage = game.new_location(
     "Stage",
     "Large stage with a wordrobe, and a passage to the west.")

barn_water = game.new_location(
     "Barn House",
     "Small barn area, there is a water fountain here.")

barn_house_on_shore = game.new_location(
     "Barn House",
     "Dirty old cabin. There is only one exit to the north.")

lake_shore = game.new_location(
    "Lake Shore",
    "This is the shore of Emigrant Lake. Emigrant Lake has been turned into acid. There is a hut to the west, and a pathway to the east.")

old_hut = game.new_location(
    "Old Hut",
    "This is an old hut on the shore.")

lake_shore1 = game.new_location(
     "lake Shore",
     "This is another part of the lake shore. There is a pathway to the east and south. !ON'TD OG OUHST! says a sighn in mysterios letters.")

terrorrized = game.new_location(
     "You Die Here",
     "The END!!!:)")

game_over_location = game.new_location(
    "You Are Dead",
    "Sorry, you have died.  There's nowhere to go except to exit the program.")

lake_shorewall = game.new_location(
    "Lake Shore",
    "This is a lake shore with a wall in front of you. There is no way around.")

lake_shore2 = game.new_location(
    "Lake Shore",
    "There is now a wall behind you that is non climable. But there is a passage to the north.")

barn_porch = game.new_location(
    "Barn Entree",
    "Small porch with a pathway leading south.")



game.new_connection("barn_entree", stage, barn_porch, [IN, WEST], [OUT])

game.new_connection("Game Over", terrorrized, game_over_location, [IN, OUT, NORTH, EAST, WEST, SOUTH, NORTH_EAST, NORTH_WEST, SOUTH_EAST, SOUTH_WEST], [NOT_DIRECTION]) 

game.new_connection("What3", lake_shore1, terrorrized, [IN, SOUTH], [OUT, NORTH])

game.new_connection("Wall", lake_shore1, lake_shorewall, [IN, EAST], [OUT, WEST])

game.new_connection("What2", lake_shore, lake_shore1, [IN, EAST], [OUT, WEST])

game.player.health = 30

game.new_connection("What1", lake_shore, old_hut, [IN, WEST], [OUT, EAST])

game.new_connection("What", barn_house_on_shore, lake_shore, [IN, NORTH], [OUT, SOUTH])

game.new_connection("Mini Barn", stage, barn_water, [IN, WEST], [OUT, EAST])

game.new_connection("Stage Way", barn, stage, [IN, NORTH], [OUT, SOUTH])

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

ropecoil = Object("rope", "long coil of rope")

pickaxe = Object("pickaxe", "smallish iron pickaxe")

open_wardrobe = False

cellar_barn.add_object(pickaxe)

def open_wardrobe(game,thing):
    global stage
    open_wardrobe = True
    game.output("You open the wardrobe revealing a coil of rope")
    stage.add_object(ropecoil)
stage.add_phrase("open wardrobe", open_wardrobe)

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

keys = Object("pair of keys", "small pair of keys")

def draw_on_whiteboard(game,thing):
    global whiteboard_markedup
    whiteboard_markedup = True
    game.output("You write on the board without thinking, it seems you wrote some sort of spell. !ERAD TI!")

marker.add_phrase(["draw on whiteboard", "draw on board"], draw_on_whiteboard)

def climb_wall(game,thing):
    global lake_shorewall
    if not "ropecoil" and "pickaxe" in game.player.inventory:
        game.output("You cannot climb this without something sharp that hooks to a rope, and a rope of course.")
    else:
        game.output("Uising the pickaxe and the rope you climb the wall.")
        player.set_location(lake_shore2)
lake_shorewall.add_phrase("climb wall", climb_wall)

storage_room1.add_object(marker)

armor = vestibule.new_object("armor", "a shiny pair of armor")

def put_on_armor(game,thing):
    game.player.health += 20
    game.output("You put the armor and become more protected.")
armor.add_phrase(["wear armor", "put on armor", "equip armor"], put_on_armor)

talk_to_man = False

old_fisherman = Actor("Old skinny fisherman")
old_fisherman.set_location(old_hut)

def talk_to_man(game,thing):
     global old_hut
     talk_to_man = True
     game.output("The old fisherman says he will trade you a fish, for a boat that will "
           "lead you back to the school. There is a fishing pole in the cellar of "
           "the cabin on the northern side of the island. Here are the keys, he sets down a pair of keys.""")
     old_hut.add_object(keys)
old_fisherman.add_phrase(["talk to man", "talk to old man", "talk to old fisherman"], talk_to_man)

talk_to_ft = False

fortune_teller = Actor("Fortune teller")
fortune_teller.set_location(terrorrized)

def talk_to_ft(game,thing):
    global terrorrized
    global playername
    talk_to_ft = True
    playerftanswer = input("Would you like me to tell you your fortune...?")
    if playerftanswer == "yes":
        game.output(playername, "Your future is that you are stuck in this room forever..."
                    "you will either quit... or restart...(: Good Bye", playername)
    else:
        game.output("Yor loss... tell me when you want to know...")

fortune_teller.add_phrase(["talk to fortune teller", "talk to ft"], talk_to_ft)

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

        game.output("the monster drops a skull key")

        lindas_room.add_object(bkey)

        morokunda.terminate()

    else:
        game.output("You have nothing strong enouph to peirce it's skin.")
        
        game.output("You have died.")
    
        player.terminate()

drink_water = False

def drink_water(game,thing):
     global barn_water
     global barn_house_on_shore
     global drink_water
     drink_water = True
     player.set_location(barn_house_on_shore)
     game.output("When drinking the water you telaport to a new place. Have a look around.")
barn_water.add_phrase("drink water", drink_water)

open_fridge = False

def open_fridge(game,thing):
     global family
     open_fridge = True
     print("You open the fridge, revealing a bottle of soda.")
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

game.add_actor(player)
game.add_actor(dog)

game.run()
