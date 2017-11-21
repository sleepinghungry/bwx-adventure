from basic_context import BasicGameWorld
from basic_context import BasicGameEngine
from basic_context import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION
from basic_context import Object, Food, Drink, Container
from basic_context import Say

world = BasicGameWorld()

# YOUR CODE STARTS HERE
# This line of code creates a location in your world.
bedroom = world.create_location("Bedroom", "a typical messy 41-year old's room")

hallway = world.create_location("Hallway", "a dark long lonely hallway")


# This line of code connects two locations together.   
door = world.create_connection("Bedroom Door", bedroom, hallway, SOUTH, NORTH)


# This line of code creates an object to pick up.
key = bedroom.create_object("small key", "a tiny silver key")


# This line of code creates a "container" that can be opened, closed, and locked.
trunk = bedroom.create_container("trunk", "a heavy trunk at the base of the bed.")


trunk.make_requirement(key)

door_key = trunk.create_object("large key", "a heavy shiny gold key")

# This line of code "locks" the door unless you have a key.
door.make_requirement(door_key)

# This line of code creates a "person" in your world.
mom = world.create_actor("mom", hallway)


# This line of code creates a custom command for the player to type in.
mom.add_phrase("chat", Say("Your mom complains about your messy room."))




# YOUR CODE ENDS HERE
game = BasicGameEngine(world)
game.run()
