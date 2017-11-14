from basic_context import BasicGameWorld
from basic_context import BasicGameEngine
from basic_context import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION
from basic_context import Say

world = BasicGameWorld()

top_deck = world.create_location("Top Deck of a Million Dollar Yacht","The salty air breezes by as you stand on the deck of the million dollar yacht.  Thhe exquisite expensiveness of this huge floatation device makes you feel dirt poor in comparison.")

below_deck = world.create_location(
  "Below Deck",
    """There is a surprisingly large hallway here.  How can something like this fit in a yacht?""")

world.create_connection("Steel Stairwell", top_deck, below_deck, [DOWN], [UP])


# Create an object in a specific location--in this case, in the vestibule
ring = top_deck.create_object("life preserver", "a red donut shape")

# Create another charactor (separate from the player) in a specific location
captain = world.create_actor("captain", top_deck)

# add a custom command and have it work only when a particular object is present--in this case, the pen.
captain.add_phrase("chat", Say("It's a fine day for a boat ride!"))

game = BasicGameEngine(world)
game.run()
