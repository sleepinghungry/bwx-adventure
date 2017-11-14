from basic_context import BasicGameWorld
from basic_context import BasicGameEngine
from basic_context import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION

world = BasicGameWorld()

# - - -

mine_enter = world.create_location("mine entrance", "you stand infront of a mine,the mine entrace faces NORTH. ")

mine_tunnle0 = world.create_location("mine tunnle", "you are in the mine now, you can see light coming from behind you form the entrance.and the tunnles, NE and NW ")

mine_tunnle1 = world.create_location("mine tunnle", "you are in compleat pich black, you can hear somthing to the left. there is a path-way to the nw")

monster_room = world.create_location("MONSTER ROOM", "there is a monster, its sleeping, watch out. ")

light_room = world.create_location("swith room", "there is a little light switch on the wall, there is a crawl way to the north")

wet_room = world.create_location("wet room", "the fllor is a a few inches deep in water, and cold wet watter driping from the celing.")

generator_room = world.create_location("generator room", "there is a huge gerator infron of you, you can see a little start sticcker above a key hole...")

globe_room = world.create_location("globe room", "there is a big globe in the middle of the room.")




# - - -

world.create_connection("door", mine_enter, mine_tunnle0, [IN, NORTH], [OUT, SOUTH]) 

world.create_connection("door", mine_tunnle0, mine_tunnle1, [IN, NORTH_EAST], [OUT, SOUTH_WEST]) 

world.create_connection("door", mine_tunnle0, monster_room, [IN, NORTH_WEST], [OUT, SOUTH_EAST])

world.create_connection("door", monster_room, light_room, [IN, NORTH_WEST], [OUT, SOUTH_EAST])

world.create_connection("door", monster_room, wet_room, [IN, NORTH_EAST], [OUT, SOUTH_WEST])

world.create_connection("door", mine_tunnle1, wet_room, [IN, NORTH_WEST], [OUT, SOUTH_EAST])

world.create_connection("crawl way", light_room, generator_room, [IN, NORTH], [OUT, SOUTH])

world.create_connection("drop", generator_room, globe_room, [IN, DOWN], [OUT, NOT_DIRECTION])




game = BasicGameEngine(world)
game.run()
