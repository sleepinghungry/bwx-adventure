from basic_context import BasicGameWorld
from basic_context import BasicGameEngine
from basic_context import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION
from basic_context import Object, Food, Drink, Container
from basic_context import Say
from basic_context import Die

world = BasicGameWorld()

# YOUR CODE STARTS HERE

# LOCATIONS
control_room = world.create_location("Control Room",
                                     """Red lights are blaring.
Most of the room is destroyed.  To the north is an engine room.
To the south lies your freedom.""")
engine_room = world.create_location("Engine Room", "Steam obscures most of the room from view.")
freedom = world.create_location("Freedom", "You are relieved to make it out alive.")


# CONNECTIONS
world.create_connection("metal gangway",control_room, engine_room, NORTH, SOUTH)
locked_door = world.create_connection("locked door", control_room, freedom, SOUTH, NORTH)

world.player.health = 50


# OBJECTS
key = control_room.create_object("silver key", "a small silver key")
box = engine_room.create_container("Silver Lock Box", "a breadbox sized silver box that looks important.") 
twizzler = Object("twizzler","a yummy red twizzler")
box.insert(twizzler)

# REQUIREMENTS
box.make_requirement(key)
locked_door.make_requirement(twizzler)

# YOUR CODE ENDS HERE
game = BasicGameEngine(world)
game.run()
