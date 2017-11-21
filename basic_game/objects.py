from basic_game.base import Base
from basic_game.interfaces import Consumable, Lightable, Lockable
from basic_game.language import proper_list_from_dict
from basic_game.writer import FEEDBACK, CONTENTS

class Object(Base):
  # name: short name of this thing
  # description: full description
  # fixed: is it stuck or can it be taken

  def __init__(self, name, desc, fixed=False):
    Base.__init__(self, name)
    self.description = desc
    self.fixed = fixed
    
  def describe(self, observer):
    if isinstance(self.description, str):
      return self.description
    else:
      return self.description(self)

class Food(Object, Consumable):
  def __init__(self, name, desc, verb, replacement = None):
    Object.__init__(self, name, desc)
    Consumable.__init__(self, verb, replacement)
    self.consume_term = "eat"
    
class Drink(Object, Consumable):
  def __init__(self, name, desc, verb, replacement = None):
    Object.__init__(self, name, desc)
    Consumable.__init__(self, verb, replacement)
    self.consume_term = "drink"

class Light(Object, Lightable):
  def __init__(self, name, description):
    Object.__init__(self, name, description)
    Lightable.__init__(self, name, Lightable.SWITCH_YES, Lightable.OFF)

        
class Container(Object, Lockable):
  def __init__(self, name, description, fixed=False):
    Object.__init__(self, name, description, fixed)
    Lockable.__init__(self)
    self.first_time = True
    self.contents = {}
    self.close()

  def insert(self, obj):
    self.contents[obj.name] = obj
    obj.game = self.game
    return obj

  def create_object(self, name, desc, fixed=False):
    return self.insert(Object(name, desc, fixed))

  def describe(self, observer, force=False):
    desc = ""   # start with a blank string

    # add the description
    if self.first_time or force:
      desc += self.description
      self.first_time = False
    else:
      desc += add_article(self.name)

    if not self.is_open():
      desc += " The %s is closed." % self.name
    else:
      desc += " The %s is open." % self.name
      # it's open so describe the contents
      desc += self.describe_contents()
    return desc
    
  def describe_contents(self):
    desc = ""
    if not self.contents:
      return desc

    writer = self.game.writer
    # try to make a readable list of the things
    contents_description = proper_list_from_dict(self.contents)
    # is it just one thing?
    if len(self.contents) == 1:
      desc += writer.style_text("\nThere is %s in the %s." % \
                                   (contents_description, self.name), CONTENTS)
    else:
      desc += writer.style_text("\nThere are a few things in the %s: %s." % \
                                   (self.name, contents_description), CONTENTS)

    return desc

  def open(self, actor):
    writer = actor.game.writer
    if self.is_open():
      writer.output("The %s is already open." % self.name)
      return True
    if not self.try_unlock(actor, writer):
      return False
    writer.output("The %s opens." % self.name, FEEDBACK)
    writer.output(self.describe_contents(), CONTENTS)
    self.unset_flag('closed')

  def close(self):
    self.set_flag('closed')

  def is_open(self):
    return not self.flag('closed')


