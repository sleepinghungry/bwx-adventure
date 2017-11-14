from basic_game.base import Base
from basic_game.verbs import BaseVerb
from basic_game.directions import directions
from basic_game.language import proper_list_from_dict

# An actor in the game
class Actor(Base):
  # location
  # inventory
  # moved
  # verbs

  def __init__(self, name, location):
    Base.__init__(self, name)
    self.health = 0
    self.location = location
    self.game = location.game
    self.allowed_locs = None
    self.inventory = {}
    self.cap_name = name.capitalize()
    self.is_player = False
    self.isare = "is"
    self.verborverbs = "s"
    self.trades = {}
    # associate each of the known actions with functions
    self.add_verb(BaseVerb(self.act_take1, 'take'))
    self.add_verb(BaseVerb(self.act_take1, 'get'))
    self.add_verb(BaseVerb(self.act_drop1, 'drop'))
    self.add_verb(BaseVerb(self.act_give, 'give'))
    self.add_verb(BaseVerb(self.act_inventory, 'inventory'))
    self.add_verb(BaseVerb(self.act_inventory, 'i'))
    self.add_verb(BaseVerb(self.act_look, 'look'))
    self.add_verb(BaseVerb(self.act_examine1, 'examine'))
    self.add_verb(BaseVerb(self.act_examine1, 'look at'))
    self.add_verb(BaseVerb(self.act_look, 'l'))
    self.add_verb(BaseVerb(self.act_go1, 'go'))
    self.add_verb(BaseVerb(self.act_eat, 'eat'))
    self.add_verb(BaseVerb(self.act_drink, 'drink'))
    self.add_verb(BaseVerb(self.act_open, 'open'))
    self.add_verb(BaseVerb(self.act_list_verbs, 'verbs'))
    self.add_verb(BaseVerb(self.act_list_verbs, 'commands'))
    
  # terminate
  def terminate(self):
    self.health = -1
    
  # describe ourselves
  def describe(self):
    return self.name

  # establish where we are "now"
  def set_location(self, loc):
    if not self.is_player and self.location:
      del self.location.actors[self.name]
    self.location = loc
    self.moved = True
    if not self.is_player:
      self.location.actors[self.name] = self

  # confine this actor to a list of locations
  def set_allowed_locations(self, locs):
    self.allowed_locs = locs

  # add something to our inventory
  def add_to_inventory(self, thing):
    self.inventory[thing.name] = thing
    return thing

  # remove something from our inventory
  def remove_from_inventory(self, thing):
    return self.inventory.pop(thing.name, None)
    
  # set up a trade
  def add_trade(self, received_obj, returned_obj, verb):
    verb.bind_to(self)
    self.trades[received_obj] = (returned_obj, verb)

  # receive a given object
  def receive_item(self, giver, thing):
    self.add_to_inventory(thing)
    if thing in self.trades.keys():
      (obj, verb) = self.trades[thing]
      verb.act(giver, thing.name, None)
      self.location.contents[obj.name] = obj
      self.remove_from_inventory(obj)

  # give something to another actor
  def act_give(self, actor, noun, words):
    d = actor.location.find_object(actor, noun)
    if not d:
      return False
    thing = d[noun]

    receiver = self
    if words:
      for w in words:
        if w in self.location.actors.keys():
          receiver = self.location.actors[w]
          break

    if not receiver:
      return False

    receiver.receive_item(actor, thing)
    del d[thing.name]
    return True
      
  # move a thing from the current location to our inventory
  def act_take1(self, actor, noun, words):
    if not noun:
      return False
    t = self.location.contents.pop(noun, None)
    if not t:
      for c in self.location.contents.values():
        if isinstance(c, Container) and c.is_open:
          t = c.contents.pop(noun, None)      
    if t:
      self.inventory[noun] = t
      self.game.writer.output("%s take%s the %s." % (actor.cap_name,
                                         actor.verborverbs,
                                         t.name))
      return True
    else:
      self.game.writer.output("%s can't take the %s." % (actor.cap_name, noun))
      return False

  # move a thing from our inventory to the current location
  def act_drop1(self, actor, noun, words):
    if not noun:
      return False
    t = self.inventory.pop(noun, None)
    if t:
      self.location.contents[noun] = t
      return True
    else:
      self.game.writer.output("{} {} not carrying {}.".format(self.cap_name,
                                                  self.isare,
                                                  add_article(noun)))
      return False

  def act_look(self, actor, noun, words):
    self.game.descriptor.output_location_description(self.location, True)
    return True

  # examine a thing in our inventory or location
  def act_examine1(self, actor, noun, words):
    if not noun:
      return False
    n = None
    if noun in self.inventory:
      n = self.inventory[noun]
    if noun in self.location.contents:
      n = self.location.contents[noun]
    for c in self.location.contents.values():
      if isinstance(c, Container) and c.is_open:
        if noun in c.contents:
          n = c.contents[noun]
    if not n:
      return False
    self.game.writer.output("You see " + n.describe(self) + ".")
    return True

  # list the things we're carrying
  def act_inventory(self, actor, noun, words):
    msg = '%s %s carrying ' % (self.cap_name, self.isare)
    if self.inventory.keys():
      msg += proper_list_from_dict(self.inventory)
    else:
      msg += 'nothing'
    msg += '.'
    self.game.writer.output(msg)
    return True

  # check/clear moved status
  def check_if_moved(self):
    status = self.moved
    self.moved = False
    return status

  # try to go in a given direction
  def act_go1(self, actor, noun, words):
    if not noun in directions:
      self.game.writer.output("Don't know how to go '{}'.".format(noun))
      return False
    loc = self.location.go(actor, directions[noun])
    if loc == None:
      self.game.writer.output("Bonk! {} can't seem to go that way.".format(self.name))
      return False
    else:
      # update where we are
      self.set_location(loc)
      return True

  # eat something
  def act_eat(self, actor, noun, words):
    d = actor.location.find_object(actor, noun)
    if not d:
      return False
    t = d[noun]
    
    if isinstance(t, Food):
      t.consume(actor, noun, words)
    else:
      self.game.writer.output("%s can't eat the %s." % (actor.name.capitalize(), noun))

    return True

  # drink something
  def act_drink(self, actor, noun, words):
    d = actor.location.find_object(actor, noun)
    if not d:
      return False
    t = d[noun]
    
    if isinstance(t, Drink):
      t.consume(actor, noun, words)
    else:
      self.game.writer.output("%s can't drink the %s." % (actor.name.capitalize(), noun))

    return True

  # open a Container
  def act_open(self, actor, noun, words):
    if not noun:
      return False
    if not noun in actor.location.contents:
      return False
    
    t = self.location.contents[noun]
    if isinstance(t, Container):
      t.open(actor)
    else:
      self.game.writer.output("%s can't open the %s." % (actor.name.capitalize(), noun))

    return True

  def act_list_verbs(self, actor, noun, words):
    things = (list(actor.inventory.values()) +
              list(actor.location.contents.values()) +
              list(actor.location.actors.values()) +
              [actor.location] + [actor])
    result = set()
    for t in things:
      for v in t.verbs.keys():
        if len(v.split()) > 1:
          result.add('"' + v + '"')
        else:
          result.add(v);
      for v in t.phrases.keys():
        if len(v.split()) > 1:
          result.add('"' + v + '"')
        else:
          result.add(v);
    self.game.writer.output(textwrap.fill(" ".join(sorted(result))))
    return True

  def lights(self, on):
      self.light_on = on
      self.game.light_changed = True

  def check_if_light_changed(self):
      changed = self.light_changed
      self.light_changed = False
      return changed

# Robots are actors which accept commands to perform actions.
# They can also record and run scripts.
class Robot(Actor):
  def __init__(self, name, location):
    Actor.__init__(self, name, location)
    self.leader = None
    self.add_verb(BaseVerb(self.act_follow, 'heel'))
    self.add_verb(BaseVerb(self.act_follow, 'follow'))
    self.add_verb(BaseVerb(self.act_stay, 'stay'))

  def act_follow(self, actor, noun, words=None):
    if noun == None or noun == "" or noun == "me":
      self.leader = self.game.player
    elif noun in self.game.robots:
      self.leader = self.game.robots[noun]
    elif noun in self.game.animals:
      self.leader = self.game.animals[noun]
    self.game.writer.output("{} obediently begins following {}".format(self.name,
                                                           self.leader.name))
    return True

  def act_stay(self, actor, noun, words=None):
    if self.leader:
      self.game.writer.output("{} obediently stops following {}".format(self.name,
                                                            self.leader.name))
    self.leader = None
    return True


# Player derives from Robot so that we can record and run scripts as the player
class Player(Robot):
  def __init__(self, location):
    Robot.__init__(self, "you", location)
    self.is_player = True
    self.isare = "are"
    self.verborverbs = ""
    self.moved = True
    
# Animals are actors which may act autonomously each turn
class Animal(Actor):
  def __init__(self, name, location):
    Actor.__init__(self, name, location)
    
  def act_autonomously(self, observer_loc):
    self.random_move(observer_loc)

  def random_move(self, observer_loc):
    if random.random() > 0.2:  # only move 1 in 5 times
      return

    # filter out any locked or forbidden locations
    exits = list()
    for (d, c) in self.location.exits.items():
      if c.is_locked():
        continue
      if c.point_b.is_locked():
        continue
      if self.allowed_locs and not c.point_b in self.allowed_locs:
        continue
      exits.append((d ,c))
    if not exits:
      return
    (exitDir, exitConn) = random.choice(exits)
    quiet = True
    if self.game.current_actor == self.game.player:
      quiet = False
    if self.game.current_actor.flag('verbose'):
      quiet = False
    if not quiet and self.location == observer_loc:
      self.game.writer.output("{} leaves the {}, heading {}.".
                  format(add_article(self.name).capitalize(),
                         observer_loc.name,
                         direction_names[exitDir].lower()))
    self.act_go1(self, direction_names[exitDir], None)
    if not quiet and self.location == observer_loc:
      self.game.writer.output("{} enters the {} via the {}.".
                  format(add_article(self.name).capitalize(),
                         observer_loc.name,
                         exitConn.name))


# A pet is an actor with free will (Animal) that you can also command to do things (Robot)
class Pet(Robot, Animal):
  def __init__(self, name, location):
    Robot.__init__(self, name, location)

  def act_autonomously(self, observer_loc):
    if self.leader:
      self.set_location(self.leader.location)
    else:
      self.random_move(observer_loc)


