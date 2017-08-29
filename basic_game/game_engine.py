from basic_game.directions import directions
from basic_game.language import list_prefix, normalize_input
from basic_game.writer import DEBUG, TITLE, ConsoleWriter

# The GameEngine: given a completed GameWorld, starts a game and runs it to
# completion.
class BasicGameEngine(object):
  def __init__(self, basic_game_world, writer=ConsoleWriter()):
    self.writer = writer
    self.current_actor = basic_game_world.player
    self.player = basic_game_world.player
    self.animals = basic_game_world.animals
    self.robots = basic_game_world.robots
    self.fresh_location = False

    self.done = False

  def output(self, text, message_type = 0):
    if message_type != DEBUG:
      self.current_actor.set_next_script_response(text)
    self.writer.output(text, message_type)
    
  @staticmethod
  def register(name, fn):
    global registered_games
    registered_games[name] = fn

  @staticmethod
  def get_registered_games():
    global registered_games
    return registered_games

  def start(self):
    self.run_room() # just set the stage before we do any scripting
    while True:
      if self.done:
          return
      self.run_room()
      if self.player.health < 0:
        self.output ("Better luck next time!")
        break
      if not self.run_step():
        break
    self.output("\ngoodbye!\n")

  def run_room(self):
    actor = self.current_actor
    if actor == self.player or actor.flag('verbose'):
      # if the actor moved, describe the room
      if actor.check_if_moved():
          self.output(actor.location.title(actor), TITLE)
        
          # cache this as we need to know it for the query to entering_location()
          self.fresh_location = actor.location.first_time
          where = actor.location.describe(actor, actor.flag('verbose'))
          if where:
            self.output("")
            self.output(where)
            self.output("")

    # See if the animals want to do anything
    for animal in self.animals.values():
      # first check that it is not dead
      if animal.health >= 0:
        animal.act_autonomously(actor.location)


  def run_step(self, cmd = None):
    self.writer.clear_text()
    actor = self.current_actor

    # check if we're currently running a script
    user_input = actor.get_next_script_command();
    if user_input == None:
      if cmd != None:
        user_input = cmd
      else:
        # get input from the user
        try:
          self.output("")  # add a blank line
          user_input = input("> ")
        except EOFError:
          return False

    # see if the command is for a robot
    if ':' in user_input:
       robot_name, command = user_input.split(':')
       try:
          actor = self.robots[robot_name]
       except KeyError:
          self.output("I don't know anybot named %s" % robot_name)
          return True
    else:
       actor = self.player
       command = user_input

    self.current_actor = actor
                
    # now we're done with punctuation and other superfluous words like articles
    command = normalize_input(command)

    # see if we want to quit
    if command == 'q' or command == 'quit':
      return False

    # give the input to the actor in case it's recording a script
    if not actor.set_next_script_command(command):
      return True

    words = command.split()
    if not words:
      return True

    # following the Infocom convention commands are decomposed into
    # VERB(verb), OBJECT(noun), INDIRECT_OBJECT(indirect).
    # For example: "hit zombie with hammer" = HIT(verb) ZOMBIE(noun) WITH HAMMER(indirect).

    # handle 'tell XXX ... "
    target_name = ""
    if words[0].lower() == 'tell' and len(words) > 2:
      (target_name, words) = get_noun(words[1:], actor.location.actors.values())

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
            return True
        else:
          f(self, thing)
          return True

    # if we have an explicit target of the VERB, do that.
    # e.g. "tell cat eat foo" -> cat.eat(cat, 'food', [])
    if target_name:
      for a in actor.location.actors.values():
        if a.name != target_name:
          continue
        v = a.get_verb(verb)
        if v:
          if v.act(a, noun, words):
            return True
      self.output("Huh? {} {}?".format(target_name, verb))
      return True

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
              return True
      for a in actor.location.actors.values():
        if indirect == a.name:
          v = a.get_verb(verb)
          if v:
            if v.act(a, noun, words):
              return True

    # if we have a NOUN, try it's handler next
    if noun:
      for thing in things:
        if noun == thing.name:
          v = thing.get_verb(verb)
          if v:
            if v.act(actor, None, words):
              return True
      for a in actor.location.actors.values():
        if noun == a.name:
          v = a.get_verb(verb)
          if v:
            if v.act(a, None, words):
              return True

    # location specific VERB
    v = actor.location.get_verb(verb)
    if v:
      if v.act(actor, noun, words):
        return True

    # handle directional moves of the actor
    if not noun:
      if verb in directions:
        actor.act_go1(actor, verb, None)
        return True

    # general actor VERB
    v = actor.get_verb(verb)
    if v:
      if v.act(actor, noun, words):
        return True

    # not understood
    self.output("Huh?")
    return True

