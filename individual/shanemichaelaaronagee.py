import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
sys.path.insert(1, os.path.join(sys.path[0], '../bwx_adventure'))
from bwx_adventure.advent import *
from bwx_adventure.advent_devtools import *

game = Game("Willow Of Death")

porch = game.new_location(
  "Porch",
  "You are on a porch. It is raining. To the North is an office door, to the west is a ramp.")

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

game.new_connection("Stairs", vestibule, upstairs, [IN, UP], [OUT, DOWN])

game.new_connection("Vestibule Door", porch, vestibule, [IN, NORTH], [OUT, SOUTH])

game.new_connection("Office Door", vestibule, office, [IN, WEST], [OUT, EAST])

family = game.new_location("Family Room",
                           "This is a large room with a fridge and an open window to the north. There is also a door to the west.")

step = game.new_location("Stepway",
                         "This is a stepway with a door to the north and west.")

game.new_connection("Ramp", porch, step, [IN, WEST], [OUT, EAST])

game.new_connection("Window", family, yard, [IN, NORTH], [OUT, SOUTH])

dog = Pet("Dog Friend")
dog.set_location()
dog.set_allowed_locations([sidewalk])

player = game.new_player(sidewalk)
sidewalk.add_object(Drink("vial",
                          "a small vial of bright green glowing liquid",
                          Die("choking violently and collapsing onto the floor..."),
                          Object("empty vial", "an empty vial with an acrid odor")))
zombie1 = Animal("zombie")
zombie1.set_location(yard)
zombie1.set_allowed_locations([yard])
game.add_actor(zombie1)
zombie1.add_phrase("wake bear",
                Die("mauled viciously by the angry bear who then falls back asleep."))  
dragon = Actor("tiny dragon")
dragon.set_location(office)
game.add_actor(dragon)
shield = vestibule.new_object("shield", "a shiny bronze sheild")
sword = office.new_object("sword", "a rusty old sword")
def fight_dragon(game, thing):
  if not "shield" in game.player.inventory:
    game.output("You try to stab the dragon with the sword, but it flames you.")
    player.terminate()
  else:
    game.output("Using the shield to avoid the dragon's flames you kill it with the sword.")
    dragon.terminate()
dragon.add_phrase("fight dragon", fight_dragon)
game.add_actor(player)
game.add_actor(cat)
test_script = Script("test",
"""
> look
> take vial
> give cat vial
> tell cat drink vial
> look
> end
""")
player.add_script(test_script)
game.run()
