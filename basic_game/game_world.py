from basic_game.writer import CONTENTS, DESCRIPTION, ConsoleWriter
from basic_game.language import proper_list_from_dict
from basic_game.base import Base
from basic_game.actors import Actor, Player, Animal, Pet
from basic_game.interfaces import Lockable
from basic_game.directions import opposite_direction
from basic_game.objects import Object

class BasicGameWorld(Base):
  def __init__(self):
    Base.__init__(self, "basic game world")
    self.objects = {}
    self.location_list = []
    self.animals = {}

    # automatically create the player
    self.player = Player()
    self.player.game = self

    # FIXME: Should ConsoleWriter be part of the GameWorld or the GameEngine?
    self.writer = ConsoleWriter()
    
  def create_location(self, *args):
    location = Location(*args)
    location.game = self
    self.location_list.append(location)

    # automatically start player in the first location created.
    if len(self.location_list) == 1:
      self.player.set_location(location)

    return location

  def create_connection(self, *args):
    connection = Connection(*args)
    connection.game = self
    if isinstance(connection.way_ab, (list, tuple)):
      for way in connection.way_ab:
        connection.point_a.add_exit(connection, way)
    else:
      connection.point_a.add_exit(connection, connection.way_ab)

    # this is messy, need a better way to do this
    reverse_connection = Connection(connection.name,
                                    connection.point_b,
                                    connection.point_a,
                                    connection.way_ba,
                                    connection.way_ab)
    reverse_connection.game = self
    if isinstance(connection.way_ba, (list, tuple)):
      for way in connection.way_ba:
        connection.point_b.add_exit(reverse_connection, way)
    else:
      connection.point_b.add_exit(reverse_connection, connection.way_ba)
    return connection

  def create_actor(self, name, location):
    actor = Actor(name, location)
    actor.game = self
    return actor
  
  def create_animal(self, name, location):
    animal = Animal(name, location)
    animal.game = self
    self.animals[name] = animal
    return animal
  
  def create_pet(self, name, location):
    pet = Pet(name, location)
    pet.game = self
    self.animals[name] = pet
    return pet

  def set_name(self, name):
    self.name = name

  def set_start_location(self, location):
    self.player.location = location


# A "location" is a place in the game.
class Location(Base, Lockable):
  # name: short name of this location
  # description: full description
  # contents: things that are in a location
  # exits: ways to get out of a location
  # first_time: is it the first time here?
  # actors: other actors in the location

  def __init__(self, name, description, inonat="in"):
    Base.__init__(self, name)
    Lockable.__init__(self)
    self.description = description
    self.inonat = inonat
    self.contents = {}
    self.exits = {}
    self.first_time = True
    self.actors = {}
    
  def create_object(self, name, desc, fixed=False):
    obj = Object(name, desc, fixed)
    self.contents[name] = obj
    obj.game = self.game
    return obj

  def title(self):
    preamble = ""
    room_name = self.name
    return "        --=( {}{} )=--        ".format(preamble, room_name)

  def description_str(self, d):
    if isinstance(d, (list, tuple)):
      desc = ""
      for dd in d:
        desc += self.description_str(dd)  # recursion!
      return desc
    else:
      if isinstance(d, str):
        return self.game.writer.style_text(d, DESCRIPTION)
      else:
        return self.description_str(d(self))

  def describe(self, force_look=False):
    desc = ""   # start with a blank string

    # add the description
    if self.first_time or force_look:
      desc += self.description_str(self.description)
      self.first_time = False

    if self.contents:
      # try to make a readable list of the things
      contents_description = proper_list_from_dict(self.contents)
      # is it just one thing?
      if len(self.contents) == 1:
        desc += self.game.writer.style_text("\nThere is {} here.".
                                  format(contents_description), CONTENTS)
      else:
        desc += self.game.writer.style_text("\nThere are a few things here: {}.".
                                     format(contents_description), CONTENTS)
      for k in sorted(self.contents.keys()):
        c = self.contents[k]
        if isinstance(c, Container) and c.is_open():
          desc += c.describe_contents()
                                     
    if self.actors:
      for k in sorted(self.actors.keys()):
        a = self.actors[k]
        if a.health < 0:
          deadornot = "lying here dead as a doornail"
        else:
          deadornot = "here"
        if a != self.game.player:
          desc += self.game.writer.style_text("\n" + add_article(a.describe()).capitalize() + \
                                       " " + a.isare + " " + deadornot + ".", CONTENTS)

    return desc

  def find_object(self, actor, name):
    if not name:
      return None
    if self.contents:
      if name in self.contents.keys():
        return self.contents
      for c in self.contents.values():
        if isinstance(c, Container) and c.is_open() and name in c.contents.keys():
          return c.contents
    if name in actor.inventory:
      return actor.inventory
    return None

  def replace_object(self, actor, old_name, new_obj):
    d = self.find_object(actor, old_name)
    if d == None:
      return None
    if not old_name in d.keys():
      return None
    old_obj = d[old_name]
    del d[old_name]
    if new_obj:
      d[new_obj.name] = new_obj
    return old_obj
    
  def add_exit(self, con, way):
    self.exits[ way ] = con

  def go(self, actor, way):
    if not way in self.exits:
      return None
    
    c = self.exits[ way ]

    # first check if the connection is locked
    if not c.try_unlock(actor, self.game.writer):
      return None

    # check if the room on the other side is locked        
    if not c.point_b.try_unlock(actor, self.game.writer):
      return None

    return c.point_b

  def debug(self):
    for key in self.exits:
      print("exit: %s" % key)

  def try_unlock(self, actor, writer):
    # first see if the actor is whitelisted
    if actor.allowed_locs:
      if not self in actor.allowed_locs:
        return False

    return super().try_unlock(actor, writer)
  
# A "connection" connects point A to point B. Connections are
# always described from the point of view of point A.
class Connection(Base, Lockable):
  # name
  # point_a
  # point_b

  def __init__(self, name, pa, pb, way_ab, way_ba=None):
    Base.__init__(self, name)
    Lockable.__init__(self)
    # way_ba defaults to the opposite of way_ab
    if way_ba is None:
        way_ba = ([opposite_direction(way) for way in way_ab]
                  if isinstance(way_ab, (list, tuple))
                  else opposite_direction(way_ab))
    self.point_a = pa
    self.point_b = pb
    self.way_ab = way_ab
    self.way_ba = way_ba
