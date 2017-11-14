from basic_context import BasicGameWorld
from basic_context import BasicGameEngine
from basic_context import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION

world = BasicGameWorld()

front_of_office = world.create_location("Front of Office","You are standing in front of a building.")

vestibule = world.create_location(
  "Vestibule",
    """A small area at the bottom of a flight of stairs.
There is a glass door to the west.""")

world.create_connection("Glass_Door", front_of_office, vestibule, [IN], [OUT])

top_of_stairs = world.create_location(
    "top of stairs",
    """A messy room full of trash and blood.there is a locked door north of where you are standing.""")

knife = top_of_stairs.create_object("bloody knife on a table", "knife")

key = top_of_stairs.create_object("key", "key")

world.create_connection ("stairs",vestibule, top_of_stairs, [UP], [DOWN])

locked_room = world.create_location(
    "locked room",
    """a room behind a locked door with a creature of some kind lying on the floor""")

world.create_connection("door",top_of_stairs, locked_room, [IN,WEST], [OUT,EAST])

door.make_requirement(key)

world.create_actor

game = BasicGameEngine(world)
game.run()
