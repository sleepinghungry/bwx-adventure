from basic_context import BasicGameWorld
from basic_context import BasicGameEngine
from basic_context import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION

world = BasicGameWorld()
Train_seat = world.create_location("train","Outside rushes by as the train slows down, door north of you")

vestibule = world.create_location(    
  "Vestibule",
    """Its PARTY TIME""")

world.create_connection = ("Place1", vestibule, Train_seat, [NORTH, OUT], [SOUTH, IN])





game = BasicGameEngine(world)
game.run()
