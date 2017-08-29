def if_flag(self, flag, s_true, s_false, location = None):
  return lambda loc: (s_false, s_true)[flag in (location or loc).vars]

def if_var(self, v, value, s_true, s_false, location = None):
    return lambda loc: (s_false, s_true)[v in (location or loc).vars and (location or loc).vars[v] == value] 

# checks to see if the inventory in the items list is in the user's inventory
def inventory_contains(self, items):
  if set(items).issubset(set(self.player.inventory.values())):
    return True
  return False

def entering_location(self, location):
  if (self.player.location == location and self.fresh_location):
      return True
  return False
  
def say(self, s):
  return lambda game: game.output(s)
