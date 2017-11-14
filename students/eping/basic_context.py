import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from basic_game.game_world import BasicGameWorld, Location, Connection
from basic_game.basic_game_engine import BasicGameEngine
from basic_game.directions import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION
from basic_game.objects import Object, Food, Drink, Light, Container
from basic_game.actors import Actor, Player, Animal, Pet
from basic_game.verbs import BaseVerb, Die, Say, SayOnNoun, SayOnSelf, Verb
from basic_game.descriptors import Descriptor
