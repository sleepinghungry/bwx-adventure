from basic_game.language import proper_list_from_dict
from basic_game.verbs import Verb

class Lockable(object):
  def __init__(self):
    self.requirements = {}
    self.locked = False
    
  def make_requirement(self, thing):
    self.requirements[thing.name] = thing
    self.lock()
      
  def lock(self):
    self.locked = True
    
  def unlock(self):
    self.locked = False
    
  def is_locked(self):
    return self.locked
    
  def try_unlock(self, actor):
    # now check if we're locked
    if not self.locked:
      return True
    
    # check if there are any implicit requirements for this object
    if len(self.requirements) == 0:
      actor.output("It's locked!")
      return False

    # check to see if the requirements are in the inventory
    if set(self.requirements).issubset(set(actor.inventory)):
      actor.output("You use the {}, the {} unlocks".
                         format(proper_list_from_dict(self.requirements),
                                self.name))
      self.unlock()
      return True

    actor.output("It's locked! You will need {}.".
                       format(proper_list_from_dict(self.requirements)))
    return False


class Consumable(object):
  def __init__(self, parent, verb, replacement = None):
    self.parent = parent
    self.verb = verb
    verb.bind_to(self)
    self.consume_term = "consume"
    self.replacement = replacement
    
  def consume(self, actor, noun, words):
    if not actor.location.replace_object(actor, self.parent.name,
                                         self.replacement):
      return False
    
    actor.output("%s %s%s %s." % (actor.name.capitalize(), self.consume_term,
                                 actor.verborverbs, self.parent.description))
    self.verb.act(actor, noun, words)
    return True
    


class Lightable(object):
  ON = "on"
  OFF = "off"
  SWITCH_YES = "yes"
  SWITCH_NO = "no"
  
  def __init__(self, start_light, switchable):
    self.status = start_light
    self.switchable = switchable
    self.add_phrase("turn on", Verb(self.act_turn_on))
    self.add_phrase("turn off", Verb(self.act_turn_off))
    
  def act_turn_on(self, actor, noun, words):
    writer = actor.game.writer
    if isinstance(self, Location):
      writer.output("Trying to turn on lights in a location...")
    elif isinstance(self, Object):
      writer.output("Trying to turn on lights for an object...")

    if not noun:
      writer.output("No noun")  
      return False

    writer.output("self.switchable is {}.".format(self.switchable))
  
    if self.switchable == self.ON:
      writer.output("There is no light switch to turn on here.")
    elif self.status == self.ON:
      if isinstance(self, Location):
        writer.output("The light is already on here.")
      else:
        writer.output("The {} is already on.".format(self.name))
    else:
      writer.output("It's switchable...")
      if noun in self.game.player.inventory:
        writer.output("Incrementing player light count")
        self.game.player.light_count += 1
      elif noun in self.game.player.location.contents:
        writer.output("Incrementing location light count")
        self.game.player.location.light_count += 1
      self.status = self.ON
      self.describe(self.ON)
      if (self.game.player.light_count + self.game.player.location.light_count) == 1:
        self.game.output_title(actor)
        self.game.output_description(actor)
    return True

  def act_turn_off(self, actor, noun, words):
    writer = actor.game.writer
    if not noun:
      return False

    writer.output("self.switchable is {}.".format(self.switchable))
    if self.switchable == self.SWITCH_NO:
      writer.output("There is no light switch to turn off here.")

    elif self.status == self.OFF:
      writer.output("The {} is already off.".format(noun))
    else:
      if noun in self.game.player.inventory:
        self.game.player.light_count -= 1
      elif noun in self.game.player.location.contents:
        self.game.player.location.light_count -= 1
      self.status = self.OFF
      self.describe(self.OFF)
      if (self.game.player.light_count + self.game.player.location.light_count) == 0:
        self.game.output_title(actor)
        self.game.output_description(actor)
    return True

  def describe(self, on_or_off, writer):
    writer.output("You turn ", on_or_off, " the ", self.name)
