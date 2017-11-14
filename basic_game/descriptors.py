from basic_game.language import proper_list_from_dict, add_article
from basic_game.writer import CONTENTS, DESCRIPTION, TITLE
from basic_game.objects import Container

class Descriptor():
  """Encapsulates the methods and logic used to describe a location."""

  def __init__(self, writer):
    self.writer = writer
    
  def output_title(self, location):
    """Return a nicely formattted title header for a location."""
    self.writer.output("        --=( {} )=--        ".format(location.name),
                       TITLE)

  def output_location_description(self, location, force_look=False):
    """Return a nicely formatted description of the location and its contents.
    """
    desc = ""   # start with a blank string

    if location.first_time or force_look:
      location.first_time = False
      desc += self._describe_location(location)

    desc += self._describe_contents(location)
    desc += self._describe_actors(location)
    
    self.writer.output(desc)
    
  def _description_str(self, d):
    """Takes a description, which can apparently be a list, tuple, string, 
    or function!!!
    Not sure why a location description would be a list or tuple, but
    a function makes sense.  You could custom describe a room based on
    a location's properties or changes in the game or player.
    """
    if isinstance(d, (list, tuple)):
      desc = ""
      for dd in d:
        desc += self._description_str(dd)  # recursion!
      return desc
    else:
      if isinstance(d, str):
        return self.writer.style_text(d, DESCRIPTION)
      else:
        return self._description_str(d(self))

  def _describe_location(self, location):
    return self._description_str(location.description)

  def _describe_contents(self, location):
    contents = location.contents
    desc = ""
    if contents:
      # try to make a readable list of the things
      contents_description = proper_list_from_dict(contents)
      # is it just one thing?
      if len(contents) == 1:
        desc += self.writer.style_text("\nThere is {} here.".
                                       format(contents_description), CONTENTS)
      else:
        desc += self.writer.style_text("\nThere are a few things here: {}.".
                                       format(contents_description), CONTENTS)
      for k in sorted(contents.keys()):
        c = contents[k]
        if isinstance(c, Container) and c.is_open():
          desc += c.describe_contents()
    return desc
          
  def _describe_actors(self, location):
    # add list of actors      
    actors = location.actors
    desc = ""
    if actors:
      for k in sorted(actors.keys()):
        a = actors[k]
        if a.health < 0:
          deadornot = "lying here dead as a doornail"
        else:
          deadornot = "here"
        if a != location.game.player:
          desc += self.writer.style_text("\n" + add_article(a.describe()).capitalize() + \
                                       " " + a.isare + " " + deadornot + ".", CONTENTS)

    return desc

