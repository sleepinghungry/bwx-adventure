from basic_context import BasicGameWorld
from basic_context import BasicGameEngine
from basic_context import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION
from basic_context import Object, Food, Drink, Container
from basic_context import Say, BaseVerb, Verb
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




ball = control_room.create_object("red ball", "a bouncy red ball")

ball.add_phrase("bounce ball", Say(["This is fun!",
                                    "This is really fun!",
                                    "This is unbelievably fun!",
                                    "This is no longer fun.",
                                    "Stop bouncing the ball!",
                                    "I swear, you've got to stop.",
                                    "Don't you have anything better to do?"]))


def mark_consumed(twizzler, actor, noun, words):
    actor.game.writer.output("That was yummy!")
    actor.set_flag("ate twizzler")

twizzler = Food("twizzler",
                "a yummy red twizzler",
                Verb(mark_consumed, "blahblah"))
box.insert(twizzler)




book = box.create_object("book", "a small book")



def ending_check(world, location):
    if world.player.flag("ate twizzler") and location.name == "Freedom":
        return True
    else:
        return False
    
# this is how to end the game
freedom.cond_end(ending_check, "Congratulations on making it out and eating the twizzler!")

# REQUIREMENTS
box.make_requirement(key)
locked_door.make_requirement(twizzler)

# YOUR CODE ENDS HERE
game = BasicGameEngine(world)
game.run()
