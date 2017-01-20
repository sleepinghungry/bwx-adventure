
#!/user/bin/python 
# vim: et sw=2 ts=2 sts=2

import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from bwx_adventure.advent import Game, Location, Connection, Object, Actor, Animal, Robot, Pet, Player, Say, SayOnNoun, SayOnSelf, Verb, Food, Drink, Container, Die
from bwx_adventure.advent import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION

game = Game("Willow Wind Adventure Demo") 
# Locations

red = game.new_location("Red Forest", "A forest with all red trees.")

orange = game.new_location("Orange Forest", "A forest with all orange trees.")

yellow = game.new_location("Yellow Forest", "A forest with all yellow  trees.")

green = game.new_location("Green Forest", "A forest with all green trees.")

blue = game.new_location("Blue Forest", "A forest with all  blue trees.")

indigo = game.new_location("Indigo Forest","A forest with all indigo  trees.")

violet = game.new_location("Violet Forest","A forest with all violet trees.")

dark = game.new_location("Dark Forest","A forest with no sight and all black features.")


           
under = game.new_location("Bottem stairway"," You are now underground")

ice = game.new_location("Ice Room","It is cold here. You will need a coat.")

speaker = game.new_location("Speaker Room","It is VERY loud! You will need something to cover your ears.")

doom = game.new_location("Doom Room","This is a damp, and lightly light room")

boss_room = game.new_location("Boss Room","There is a big, mean, boss dragon. Watch out!")

mine = game.new_location("The Mine Room","It is damp down here.")

hole = game.new_location("The Black Hole"," ")

upstairs = game.new_location("upstairs Hall", "You are upstairs")

room_5 = game.new_location("Computer Lab","You are now in a big room with computers everywhere.")

playground = game.new_location("Playground","This is the playground.it is very colerful")

blacktop = game.new_location("Blacktop","The blacktop is a larg area of black concreat")

room_4 = game.new_location("Room 4","This is a small room")

room_3 = game.new_location("Room 3","This room is very bright and sunny")

room_1 = game.new_location("Room 1","There is a bathroom to your left, and infront of you is desks and a screen")          

barn = game.new_location("Barn","There is a portal spinning in the corner. Exits  on the north and west sides.")

#Items

amathyst = mine.new_object("Amathyst","A beautiful shiny purple rock!")      

headphones = room_5.new_object("Headphones","Plain black headphones.")

micro_chip = room_5.new_object("Micro chip","A small, nifty little thing!")

rope = room_3.new_object("rope","A tough, thick rope.")

warm_coat = room_1.new_object("Warm coat","A fuzzy wohle coat.")

picaxe = playground.new_object("Picaxe","A sharp stone picaxe.")

sword = room_4.new_object("Sword","Here is a metel sword with a sharp point.")

key = boss_room.new_object("Key","A old key made of bone.")


red_dye = red.new_object("Red Dye","A color as colorful as a seting sun!")

orange_dye = orange.new_object("Orange Dye","An orange as bright as the sunset!")

yellow_dye = yellow.new_object("Yellow Dye","As warm and beautiful as the sun!")

green_dye = green.new_object("Green Dye"," As green as lush grass!")

blue_dye = blue.new_object("Blue Dye","The coler of the bluest skys!")  

indigo_dye = indigo.new_object("Indigo Dye","The coler of ripe blueberies")           

violet_dye = violet.new_object("Violet Dye","As puple as Vilets!") 

pot = dark.new_object("Pot","A black culdren that looks like it was recently used.")

# Connection
game.new_connection("stairs",dark, upstairs, DOWN, UP)         

game.new_connection("blacktop",blacktop, room_5, EAST, WEST)

game.new_connection("blacktop",room_5, barn, EAST, WEST)

game.new_connection("blacktop",barn, room_1, WEST, SOUTH)

game.new_connection("blacktop",room_1, blacktop , NORTH, SOUTH)

game.new_connection("blacktop",room_1, room_3, WEST, EAST)

game.new_connection("blacktop",room_3, room_4, NORTH, SOUTH)

game.new_connection("Wood chips",room_4, blacktop, EAST, WEST)

game.new_connection("Wood chips",room_4, playground, NORTH, SOUTH)


game.new_connection("portal",barn, dark, DOWN, UP)

game.new_connection("forest",dark, blue, SOUTH,SOUTH)

game.new_connection("forest",blue, indigo, EAST, WEST)

game.new_connection("forest",blue, yellow, WEST, EAST)

game.new_connection("forest",yellow,red, NORTH, WEST)   

game.new_connection("forest",red, green, NORTH, SOUTH)

game.new_connection("forest",green, orange, WEST, EAST)                                                                                                                             

game.new_connection("forest", green, violet, EAST, WEST)

game.new_connection("forest", orange, violet, NORTH, NORTH)                       

game.new_connection("forest", violet, indigo, NORTH, SOUTH)


game.new_connection("hallway", upstairs, ice, NORTH, WEST)

game.new_connection("hallway", ice, speaker, NORTH, SOUTH)

game.new_connection("hallway",speaker, doom, WEST, NORTH)

game.new_connection("hallway", ice, boss_room, EAST, WEST)                                           

game.new_connection("hallway", boss_room, mine, NORTH, WEST)                                                                               

mine_bkhl = game.new_connection("hallway", mine, hole, SOUTH, NOT_DIRECTION)                                                                                    
    
def fightmonster(game, thing):
  if random.random()>0.8:
    thing.health-=1
  else:  
    game.player.health-=1,Say("your dead! deal with it")
game.new_player(blacktop)            
game.run()
