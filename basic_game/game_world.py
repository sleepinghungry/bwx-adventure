from basic_game.writer import CONTENTS, DESCRIPTION, ConsoleWriter
from basic_game.language import proper_list_from_dict
from basic_game.base import Base
from basic_game.actors import Actor, Player, Animal, Pet
from basic_game.interfaces import Lockable
from basic_game.directions import opposite_direction
from basic_game.objects import Object, Container
from basic_game.descriptors import Descriptor

class BasicGameWorld(Base):
  """Contains both the physical layout of the game world and methods for
  creating and expanding it.
  """
  def __init__(self):
    Base.__init__(self, "basic game world")
    self.location_list = []
    self.animals = {}
    self.player = Player(self)
    
    # FIXME: Should ConsoleWriter be part of the GameWorld or the GameEngine?
    self.writer = ConsoleWriter()
    self.descriptor = Descriptor(self.writer)
    
  def create_location(self, *args):
    """Creates a location and stores it in the location_list."""
    location = Location(*args)
    location.game = self
    self.location_list.append(location)

    # automatically start player in the first location created.
    if len(self.location_list) == 1:
      self.player.set_location(location)
      self.player.game = location.game

    return location

  def create_connection(self, *args):
    """Creates a connnection between two locations."""
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

  def set_start_location(self, location):
    """Changes the player's start location."""
    self.player.location = location

  def create_actor(self, name, location):
    """Creates an actor at a specific location."""
    actor = Actor(name, location)
    location.actors[name] = actor
    return actor
  
  def create_animal(self, name, location):
    """Creates and animal at a specific location and stores the animal in
    the animals list.
    """
    animal = Animal(name, location)
    self.animals[name] = animal
    location.actors[name] = animal
    return animal
  
  def create_pet(self, name, location):
    """Creates a pet at a specific location and stores the pet in the animals
    list.
    """
    pet = Pet(name, location)
    self.animals[name] = pet
    location.actors[name] = pet
    return pet


class Location(Base, Lockable):
  """A location is a place in the game world.
  name: short name of this location
  description: full description
  contents: things that are in a location
  exits: ways to get out of a location
  first_time: is it the first time here?
  actors: other actors in the location
  """

  def __init__(self, name, description, inonat="in"):
    Base.__init__(self, name)
    Lockable.__init__(self)
    self.description = description
    self.inonat = inonat
    self.contents = {}
    self.exits = {}
    self.first_time = True
    self.actors = {}
    self.game_end = None
    
  def create_object(self, name, desc, fixed=False):
    obj = Object(name, desc, fixed)
    self.contents[name] = obj
    obj.game = self.game
    return obj

  def create_container(self, name, desc, fixed=False):
    container = Container(name, desc, fixed)
    self.contents[name] = container
    container.game = self.game
    return container

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

  def try_unlock(self, actor, writer):
    # first see if the actor is whitelisted
    if actor.allowed_locs:
      if not self in actor.allowed_locs:
        return False

    return super().try_unlock(actor, writer)


 
class Connection(Base, Lockable):
  """A "connection" connects point A to point B. Connections are
  always described from the point of view of point A.
  """

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
