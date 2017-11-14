import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
sys.path.insert(1, os.path.join(sys.path[0], '../../bwx_adventure'))
from bwx_adventure.advent import *
from bwx_adventure.advent_devtools import *

game = Game("Survival Mt.Z")

game.new_location("Dock of Pond",
                  "")
