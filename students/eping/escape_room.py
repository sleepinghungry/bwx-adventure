from basic_context import BasicGameWorld
from basic_context import BasicGameEngine
from basic_context import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION
from basic_context import Object, Food, Drink, Container
from basic_context import Say
from basic_context import Die

world = BasicGameWorld()
world.player.health = 100

# YOUR CODE STARTS HERE

# LOCATIONS
control_room = world.create_location("Control Room",
                                     """Red lights are blaring.  The roof is on fire.  You should probably leave.
To the north is a gangway leading to the engine room.  To the south is a door to the outside.  There is also a bathroom.""")
engine_room = world.create_location("Engine Room", "Steam obscures most of the room from view.  There may be other ways out other than the one you came through.  But can't see them.")
bathroom = world.create_location("Bathroom", "A surprisingly clean bathroom, given the circumstances.")
mess_hall = world.create_location("Mess Hall", "Like it's name, messy.  There doesn't appear to be any food.")
freedom = world.create_location("Freedom", "You are relieved to make it out alive.")


# CONNECTIONS
metal_gangway = world.create_connection("metal gangway",control_room, engine_room, NORTH, SOUTH)
locked_door = world.create_connection("locked door", control_room, freedom, SOUTH, NORTH)
sliding_door = world.create_connection("sliding door", control_room, bathroom, WEST, EAST)
double_doors = world.create_connection("double doors", engine_room, mess_hall, WEST, EAST)


# OBJECTS
silver_key = mess_hall.create_object("silver key", "a small silver key")
silver_box = engine_room.create_container("Silver Lock Box", "a breadbox sized silver box that looks important.") 
gold_key = engine_room.create_object("gold key", "a scratched up gold key")
wooden_key = bathroom.create_object("wooden key", "a poorly made wooden key")
twizzler = silver_box.create_object("twizzler","a yummy red twizzler")
silver_box.insert(twizzler)

# REQUIREMENTS
silver_box.make_requirement(silver_key)
mess_hall.make_requirement(gold_key)
engine_room.make_requirement(wooden_key)
locked_door.make_requirement(twizzler)

# YOUR CODE ENDS HERE
game = BasicGameEngine(world)
game.run()
