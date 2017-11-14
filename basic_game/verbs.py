class BaseVerb():
  def __init__(self, function, name):
    self.name = name
    self.function = function 
    self.bound_to = None
    
  def bind_to(self, obj):
    self.bound_to = obj
    
  def act(self, actor, noun, words):
    result = True
    if not self.function(actor, noun, None):
      result = False
    # treat 'verb noun1 and noun2..' as 'verb noun1' then 'verb noun2'
    # treat 'verb noun1, noun2...' as 'verb noun1' then 'verb noun2'
    # if any of the nouns work on the verb consider the command successful,
    # even if some of them don't
    if words:
      for noun in words:
        if self.function(actor, noun, None):
          result = True
    return result


class Die(BaseVerb):
  def __init__(self, string, name = ""):
    BaseVerb.__init__(self, None, name)
    self.string = string

  def act(self, actor, noun, words):
    self.bound_to.game.writer.output("{} {} {}".format(actor.name.capitalize(),
                                            actor.isare, self.string))
    self.bound_to.game.writer.output("{} {} dead.".format(actor.name.capitalize(),
                                                   actor.isare))
    actor.terminate()
    return True

class Say(BaseVerb):
  def __init__(self, string, name = ""):
    BaseVerb.__init__(self, None, name)
    self.string = string
    self.index = 0

  def act(self, actor, noun, words):
    result = self.string
    if isinstance(self.string, (list, tuple)):
      if self.index < len(self.string):
        result = self.string[self.index]
        self.index += 1
      else:
        result = self.string[-1]
    self.bound_to.game.writer.output(result)
    return True

class SayOnNoun(Say):    
  def __init__(self, string, noun, name = ""):
    Say.__init__(self, string, name)
    self.noun = noun

  def act(self, actor, noun, words):
    if self.noun != noun:
      return False
    self.bound_to.game.writer.output(self.string)
    return True

class SayOnSelf(SayOnNoun):
  def __init__(self, string, name = ""):
    SayOnNoun.__init__(self, string, None, name)

# Verb is used for passing in an unbound global function to the constructor
class Verb(BaseVerb):
  def __init__(self, function, name = ""):
    BaseVerb.__init__(self, function, name)

  # explicitly pass in self to the unbound function
  def act(self, actor, noun, words):
    return self.function(self.bound_to, actor, noun, words)

