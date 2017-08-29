import sys

FEEDBACK = 0
TITLE = 1
DESCRIPTION = 2
CONTENTS = 3
DEBUG = 4

class Colors:
  '''
  Colors class:
  reset all colors with colors.reset
  two subclasses fg for foreground and bg for background.
  use as colors.subclass.colorname.
  i.e. colors.fg.red or colors.bg.green
  also, the generic bold, disable, underline, reverse, strikethrough,
  and invisible work with the main class
  i.e. colors.bold
  '''
  reset='\033[0m'
  bold='\033[01m'
  disable='\033[02m'
  underline='\033[04m'
  reverse='\033[07m'
  strikethrough='\033[09m'
  invisible='\033[08m'
  class FG:
    black='\033[30m'
    red='\033[31m'
    green='\033[32m'
    orange='\033[33m'
    blue='\033[34m'
    purple='\033[35m'
    cyan='\033[36m'
    lightgrey='\033[37m'
    darkgrey='\033[90m'
    lightred='\033[91m'
    lightgreen='\033[92m'
    yellow='\033[93m'
    lightblue='\033[94m'
    pink='\033[95m'
    lightcyan='\033[96m'
  class BG:
    black='\033[40m'
    red='\033[41m'
    green='\033[42m'
    orange='\033[43m'
    blue='\033[44m'
    purple='\033[45m'
    cyan='\033[46m'
    lightgrey='\033[47m'

class ConsoleWriter(object):
  def __init__(self):
    self.debug_level = 10
    # Generally, don't color text or background.  But, if the module is running
    # on Mac in something other than idle, then it is OK to use color.
    self.use_color_text = False
    if sys.platform == 'darwin' and 'idlelib' not in sys.modules:
      self.use_color_text = True

  def output(self, text, message_type = 0):
    self.print_output(text, message_type)

  def debug(self, text, level = 0):
    if self.debug_level >= level:
      self.output(text, DEBUG)
    return
    
  def clear_text(self):
      pass
    
  def style_text(self, text, message_type):
    if self.use_color_text:
      if (message_type == FEEDBACK):
        text = Colors.FG.pink + text + Colors.reset
      if (message_type == TITLE):
        text = Colors.FG.yellow + Colors.BG.blue + "\n" + text + Colors.reset
      if (message_type == DESCRIPTION):
        text = Colors.reset + text
      if (message_type == CONTENTS):
        text = Colors.FG.green + text + Colors.reset
      if (message_type == DEBUG):
        text = Colors.bold + Colors.FG.black + Colors.BG.orange + "\n" + text + Colors.reset
    return text

  def print_output(self, text, message_type = 0):
    print(self.style_text(text, message_type))
