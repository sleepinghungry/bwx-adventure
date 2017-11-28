from basic_context import BasicGameWorld
from basic_context import BasicGameEngine
from basic_context import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION
from basic_context import Die
import random
import time

world = BasicGameWorld()

front_of_office = world.create_location("door of dungeon","You are standing in front of the entrance to a dark, deep, musty dungeon.")

world.player.health = 50

vestibule = world.create_location(
  "entry room",
    """A small area at the top of a long flight of stairs. Writing on one wall says BEWARE ALL  WHO ENTER THIS ACCURSED PLACE. THOSE WHO DO NOT HEED THIS WARNING SHALL DIE.""")

world.create_connection("Glass_Door", front_of_office, vestibule, [IN], [OUT])

top_of_stairs = world.create_location(
    "bottom of stairs",
    """A messy room full of trash and blood.there is a locked door north of where you are standing.""")

knife = top_of_stairs.create_object("knife", "bloody knife on a table")

key = top_of_stairs.create_object("key", "heavy-looking key shaped like a stylized sword")

world.create_connection ("stairs",vestibule, top_of_stairs, DOWN,UP)

locked_room = world.create_location(
    "locked room",
    """a room behind a locked door with a creature of some kind lying on the floor and a way out to the south""")

door = world.create_connection("door",top_of_stairs, locked_room, [IN,WEST], [OUT,EAST])

bug = world.create_actor("bugbear", locked_room)
bug.health=10
def fight_bugbear(game, thing):
    bug.health -= 5
    game.player.health -= random.randint(5,15)
    if bug.health >=0:
        bug.terminate
        print ("you killed the bugbear, but took damage  in the process. you have",game.player.health,"health left") 
    if game.player.health >=0:
        Die ("the bugbear slashed you open with its claws. as you pass from this world, the last thing you see is the bugbear lying dead on the ground before you. you smile at death, knowing you have defeated your last opponent") 

bug.add_phrase("fight bugbear",fight_bugbear)       

door.make_requirement(key)

skeleton_room = world.create_location (
    "skeleton room",
    """ a room full of bones with 3 complete skeletons among them. these say skeleton1, skeleton2, and skeleton3. as you enter, skeleton1 rises off the ground saying 'die, tresspasser!'""")
skel1 = world.create_actor("skeleton1", skeleton_room)

skel1.health=25
def fight_skeleton1(game, thing):
    skel1.health -= random.randint(10,25)
    game.player.health -= random.randint(5,15)
    if skel1.health >=0:
        skel1.terminate
        print ("you killed skeleton1, but took damage  in the process. you have",game.player.health,"health left") 
    if game.player.health >=0:
        Die ("skeleton1 slashed you open with its claws. as you pass from this world, the last thing you see is skeleton1 lying dead on the ground before you. you smile at death, knowing you have defeated your last opponent") 
skel1.add_phrase("fight skeleton1",fight_skeleton1)       

world.create_connection("passageway", locked_room, skeleton_room, SOUTH,NORTH)

def describe_bobroom(game):
    game.writer.output("this world will now print 'bob' 7000000000 times. \n gameplay will resume when this objective has been completed")
    time.sleep(10)
    for i in range (1,7000000000):
        game.writer.output("bob")

bobroom = world.create_location(
    "bob room",
    describe_bobroom)
world.create_connection("down", bobroom, skeleton_room, OUT, IN)




game = BasicGameEngine(world)
game.run()
