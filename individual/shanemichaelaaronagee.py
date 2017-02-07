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

game.new_location(
office = game.new_location(
  "Office",
"""A nicely organized office.
There is a door to the north.""")

game.new_connection("Vestibule Door", porch, vestibule, [IN, NORTH], [OUT, SOUTH])

game.new_connection("Office Door", vestibule, office, [IN, WEST], [OUT, EAST])

cat = Pet("cat")
cat.set_location(sidewalk)
cat.set_allowed_locations([sidewalk])

player = game.new_player(sidewalk)
sidewalk.add_object(Drink("vial",
                          "a small vial of dark sinister looking liquid",
                          Die("choking violently and collapsing onto the floor..."),
                          Object("empty vial", "an empty vial with an acrid odor")))
bear = Animal("sleeping bear")
bear.set_location(vestibule)
bear.set_allowed_locations([vestibule])
game.add_actor(bear)
bear.add_phrase("wake bear",
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
