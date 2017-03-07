import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from bwx_adventure.advent import Game, Location, Connection, Object, Animal, Robot, Pet, Player, Actor, Verb, Say, SayOnNoun, SayOnSelf, Container, Food, Drink, Die
from bwx_adventure.advent import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION


game = Game("Brightworks Adventure")



sidewalk = game.new_location(
  "DYLANS BRAIN",
  """WELCOME TO SESAME STREET A DANGEROUS PARALLEL UNIVERSE ,TRY TO SURVIVE... IF YOU CAN. THE EXIT IS EAST LEAVE BEFORE IT IS TO LATE""")


vestibule = game.new_location(
  "CANADA",
"""HA HA HA *you hear evil laughter*,ITS A TRAP NOW YOU WILL GET EATEN ALIVE BY UNICORNS BOI... YOU SEE A HERD OF UNICORNS OVER THE HORIZON, RUN NORTH!!!""")


game.new_connection("POO BRICK", sidewalk, vestibule, EAST, WEST)



player = game.new_player(sidewalk)


apocalypse = game.new_location(
    " apocalypse",
    """ whew, your not in dylan's brain. Trust me it's safer here. OH NO HE'S COMING...JOHN CENA! """)
game.new_connection("HOLE IN THE GROUND", vestibule, apocalypse, NORTH, SOUTH)
arm = apocalypse.new_object("arm of elmo","a mighty weapon")

arm.add_phrase("attack",Say("you feel like a crazy idiot, Now with your mighty weapon you must conquer the unicorns"))

unicorn_herd = Actor("unicorn herd")

unicorn_herd.set_location(vestibule)

ELMOS_FORT = game.new_location(
"ELMO'S FORT",
"""*YOU EMERGE IN A WELL LIT WINDOWLESS ROOM, YOU SEE A MAN ACROSS THE ROOM*""")
game.new_connection("HORSE'S BUTT", vestibule,ELMOS_FORT , SOUTH, UP)

unicorn_herd.add_phrase("chat",Say("*the unicorn herd stops next to you* THE FRONT UNICORN RELEASES AN EAR PEARCING SCREECH,VRUN TINY PREEY VE VILL HUNT JOU"))


game.run()
