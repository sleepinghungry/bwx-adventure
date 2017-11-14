from basic_context import BasicGameWorld
from basic_context import BasicGameEngine
from basic_context import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION
from basic_context import Object

world = BasicGameWorld()

puffy_cloud = world.create_location("puffy cloud","a cloud with a tall ladder reaching up to more clouds.")

puffy_cloud.create_object("key", "small rubbed-down silver key") 
gray_rain_cloud = world.create_location(
  "gray rain cloud",
    """a larger cloud that looks gray and sad. small raindrops are falling. It starts raining hard now, and there is no other way to go but down with the rain""")

world.create_connection("ladder", puffy_cloud, gray_rain_cloud, [IN, UP], [OUT, DOWN])

# Hi Flannery--Eping here.  I mistakenly merged an old version of your game with your most recent version...
# so these next two lines of code may not have been here when you last worked on this file.
# I left them in just in case. Sorry!  
museum = world.create_location("museum", "the rain takes you down as the cloud falls apart. you fall and fall untill you are sucked through a chimney leading into a museum. You climb out and find yourself in a huge room with dinosaur skeletons everywhere. There's a hallway to your right, door to your left, and a flight of stairs leading up")

world.create_connection("rain", gray_rain_cloud, museum, [IN, DOWN], [NOT_DIRECTION]) 

game = BasicGameEngine(world)
game.run()
