from basic_game.verbs import BaseVerb
from basic_game.writer import DESCRIPTION

class GameEnding(object):
  """Contains text and a custom function to see if the game has reached an
  end point or not."""
  def __init__(self):
    self.text = None
    self.check = None
    
  def reached(self):
    if self.run_check:
      return self.check()
    else:
      return True


class Base(object):
  """ Contains default implmenetations of methods that everything in the 
      game should support (eg save/restore, how to respond to verbs, etc.)
  """

  def __init__(self, name):
    self.game = None
    self.name = name
    self.game_end = None
    self.verbs = {}
    self.phrases = {}
    self.vars = {}

  def flag(self, f):
    if f in self.vars:
      return self.vars[f]
    else:
      return False

  def set_flag(self, f):
    self.vars[f] = True

  def unset_flag(self, f):
    if f in self.vars:
      del self.vars[f]

  def var(self, var):
    if var in self.vars:
      return self.vars[var]
    else:
      return None

  def set_var(self, var, val):
    self.vars[var] = val

  def unset_var(self, var):
    if var in self.vars:
      del self.vars[var]

  def add_verb(self, v):
    self.verbs[' '.join(v.name.split())] = v
    v.bind_to(self)
    return v

  def get_verb(self, verb):
    c = ' '.join(verb.split())
    if c in self.verbs:
       return self.verbs[c]
    else:
      return None

  def add_phrase(self, phrase, f, requirements = []):
    print("Base.add_phrase being called for", self.name)
    if isinstance(f, BaseVerb):
      f.bind_to(self)
    if isinstance(phrase, (list, tuple)):
      for phr in phrase:
        self.phrases[' '.join(phr.split())] = (f, set(requirements))
    else:
      self.phrases[' '.join(phrase.split())] = (f, set(requirements))

  def get_phrase(self, phrase, things_present):
    phrase = phrase.strip()
    things_present = set(things_present)
    if not phrase in self.phrases:
      return None
    p = self.phrases[phrase]
    if things_present.issuperset(p[1]):
      return p[0]
    return None

  def output(self, text, text_type=DESCRIPTION):
    """Convenience method for outputting text."""
    self.game.writer.output(text, text_type)

  def end(self, text):
    """Marks this location as a game ending location."""
    self.game_end = GameEnding()
    self.game_end.text = text
    def f():
      return True
    self.game_end.check = f

  def cond_end(self, f, text):
    self.game_end = GameEnding()
    self.game_end.text = text
    self.game_end.check = f
