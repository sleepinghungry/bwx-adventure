# "directions" are all the ways you can describe going some way; 
# they are code-visible names for directions for adventure authors
direction_names = ["NORTH","SOUTH","EAST","WEST","UP","DOWN","RIGHT","LEFT",
                   "IN","OUT","FORWARD","BACK",
                   "NORTHWEST","NORTHEAST","SOUTHWEST","SOUTHEAST"]
direction_list  = [ NORTH,  SOUTH,  EAST,  WEST,  UP,  DOWN,  RIGHT,  LEFT,
                    IN,  OUT,  FORWARD,  BACK,
                    NORTHWEST,  NORTHEAST,  SOUTHWEST,  SOUTHEAST] = \
                    range(len(direction_names))
NOT_DIRECTION = None

# some old names, for backwards compatibility
(NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST) = \
             (NORTHWEST, NORTHEAST, SOUTHWEST, SOUTHEAST)

directions = dir_by_name = dict(zip(direction_names, direction_list))


def define_direction (number, name):
    if name in dir_by_name:
        exit("%s is already defined as %d" % (name, dir_by_name[name]))
    dir_by_name[name] = number

def lookup_dir (name):
    return dir_by_name.get(name, NOT_DIRECTION)

# add lower-case versions of all names in direction_names
for name in direction_names:
    define_direction(dir_by_name[name], name.lower())

# add common aliases:
# maybe the alias mechanism should be a more general
# (text-based?) mechanism that works for any command?!!!
common_aliases = [
    (NORTH, "n"),
    (SOUTH, "s"),
    (EAST, "e"),
    (WEST, "w"),
    (UP, "u"),
    (DOWN, "d"),
    (FORWARD, "fd"),
    (FORWARD, "fwd"),
    (FORWARD, "f"),
    (BACK, "bk"),
    (BACK, "b"),
    (NORTHWEST,"nw"),
    (NORTHEAST,"ne"),
    (SOUTHWEST,"sw"),
    (SOUTHEAST, "se")
]

for (k,v) in common_aliases:
    define_direction(k,v)

# define the pairs of opposite directions
opposite_by_dir = {}

def define_opposite_dirs (d1, d2):
  for dir in (d1, d2):
    opposite = opposite_by_dir.get(dir)
    if opposite is not None:
      exit("opposite for %s is already defined as %s" % (dir, opposite))
  opposite_by_dir[d1] = d2
  opposite_by_dir[d2] = d1

opposites = [(NORTH, SOUTH),
             (EAST, WEST),
             (UP, DOWN),
             (LEFT, RIGHT), 
             (IN, OUT),
             (FORWARD, BACK),
             (NORTHWEST, SOUTHEAST),
             (NORTHEAST, SOUTHWEST)]

for (d1,d2) in opposites:
  define_opposite_dirs(d1,d2)

def opposite_direction (dir):
  return opposite_by_dir[dir]
