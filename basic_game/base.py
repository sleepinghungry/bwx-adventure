from basic_game.verbs import BaseVerb

class Base(object):
  """ Contains default implmenetations of methods that everything in the 
      game should support (eg save/restore, how to respond to verbs, etc.)
  """

  def __init__(self, name):
    self.game = None
    self.name = name
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

