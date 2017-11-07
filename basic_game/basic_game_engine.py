from basic_game.directions import directions
from basic_game.language import list_prefix, normalize_input
from basic_game.writer import DEBUG, TITLE, ConsoleWriter

class BasicGameEngine(object):
  """Given a completed GameWorld, can be used to start a game or write text
  to standard output.
  """
  
  def __init__(self, basic_game_world, writer=ConsoleWriter()):
    self.writer = writer
    self.player = basic_game_world.player
    self.animals = basic_game_world.animals
    self.done = False


  def output(self, text, message_type = 0):
    """Writes formatted game descriptions to the user. """
    self.writer.output(text, message_type)


  def run(self):
    """Run the main loop until game is done.
    """
    while not self.done:
      
      self._describe_setting()

      if self.player.health < 0:
        self.output ("Better luck next time!")
        break

      command = self._get_input()

      if command == 'q' or command == 'quit':
        break 
      
      self._do_action(command)
      
    self.output("\ngoodbye!\n")


  def _describe_setting(self):
    """Describe the new setting and actors that the player has encountered.
    """
    actor = self.player
    # if the actor moved, describe the room
    if actor.check_if_moved():
      self.output(actor.location.title(), TITLE)
      
      where = actor.location.describe()
      if where:
        self.output("")
        self.output(where)
        self.output("")
      
    # See if the animals want to do anything
    for animal in self.animals.values():
      # first check that it is not dead
      if animal.health >= 0:
        animal.act_autonomously(actor.location)
        

  def _get_input(self):
    """ Request and parse out player input."""
    self.writer.clear_text()
    self.output("")

    user_input = input("> ")

    # remove punctuation and unecessary words
    command = normalize_input(user_input)

    return command

  def _do_action(self, command):
    actor = self.player
    
    words = command.split()
    if not words:
      return
    
    # following the Infocom convention commands are decomposed into
    # VERB(verb), OBJECT(noun), INDIRECT_OBJECT(indirect).
    # For example: "hit zombie with hammer" = HIT(verb) ZOMBIE(noun) WITH HAMMER(indirect).
    things = list(actor.inventory.values()) + \
      list(actor.location.contents.values()) + \
      list(actor.location.exits.values()) + \
      list(actor.location.actors.values()) + \
      [actor.location] + \
      [actor]

    for c in actor.location.contents.values():
        if isinstance(c, Container) and c.is_open:
          things += c.contents.values()
      
    potential_verbs = []
    for t in things:
      potential_verbs += t.verbs.keys()

    # extract the VERB
    verb = None
    potential_verbs.sort(key=lambda key : -len(key))
    for v in potential_verbs:
      vv = v.split()
      if list_prefix(vv, words):
        verb = v
        words = words[len(vv):]
    if not verb:
      verb = words[0]
      words = words[1:]

    # extract the OBJECT
    noun = None
    if words:
      (noun, words) = get_noun(words, things)

    # extract INDIRECT (object) in phrase of the form VERB OBJECT PREPOSITION INDIRECT
    indirect = None
    if len(words) > 1 and words[0].lower() in prepositions:
      (indirect, words) = get_noun(words[1:], things)

    # first check phrases
    for thing in things:
      f = thing.get_phrase(command, things)
      if f:
        if isinstance(f, BaseVerb):
          if f.act(actor, noun, words):
            return
        else:
          f(self, thing)
          return

    # if we have an INDIRECT object, try it's handle first
    # e.g. "hit cat with hammer" -> hammer.hit(actor, 'cat', [])
    if indirect:
      # try inventory and room contents
      things = list(actor.inventory.values()) + \
               list(actor.location.contents.values())
      for thing in things:
        if indirect == thing.name:
          v = thing.get_verb(verb)
          if v:
            if v.act(actor, noun, words):
              return
      for a in actor.location.actors.values():
        if indirect == a.name:
          v = a.get_verb(verb)
          if v:
            if v.act(a, noun, words):
              return

    # if we have a NOUN, try it's handler next
    if noun:
      for thing in things:
        if noun == thing.name:
          v = thing.get_verb(verb)
          if v:
            if v.act(actor, None, words):
              return
      for a in actor.location.actors.values():
        if noun == a.name:
          v = a.get_verb(verb)
          if v:
            if v.act(a, None, words):
              return

    # location specific VERB
    v = actor.location.get_verb(verb)
    if v:
      if v.act(actor, noun, words):
        return

    # handle directional moves of the actor
    if not noun:
      if verb in directions:
        actor.act_go1(actor, verb, None)
        return

    # general actor VERB
    v = actor.get_verb(verb)
    if v:
      if v.act(actor, noun, words):
        return

    # not understood
    self.output("Huh?")
    return

