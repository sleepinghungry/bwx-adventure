import string

articles = ['a', 'an', 'the']
# some prepositions to recognize indirect objects in prepositional phrases
prepositions = ['aboard', 'about', 'above', 'across', 'after', 'against', 'along'
    'among', 'around', 'at', 'atop', 'before', 'behind', 'below', 'beneath',
    'beside', 'besides', 'between', 'beyond', 'by', 'for', 'from', 'in', 'including'
    'inside', 'into', 'on', 'onto', 'outside', 'over', 'past', 'than' 'through', 'to',
    'toward', 'under', 'underneath',  'onto', 'upon', 'with', 'within']


# changes "lock" to "a lock", "apple" to "an apple", etc.
# note that no article should be added to proper names;
# For now we'll just assume
# anything starting with upper case is proper.
# Do not add an article to plural nouns.
def add_article (name):
  # simple plural test
  if len(name) > 1 and name[-1] == 's' and name[-2] != 's':
    return name
  # check if there is already an article on the string
  if name.split()[0] in articles:
    return name
  consonants = "bcdfghjklmnpqrstvwxyz"
  vowels = "aeiou"
  if name and (name[0] in vowels):
     article = "an "
  elif name and (name[0] in consonants):
     article = "a "
  else:
     article = ""
  return "%s%s" % (article, name)


def normalize_input(text):
  superfluous = articles +  ['and']
  rest = []
  for word in text.split():
    word = "".join(l for l in word if l not in string.punctuation)
    if word not in superfluous:
      rest.append(word)
  return ' '.join(rest)


def proper_list_from_dict(d):
  names = d.keys()
  buf = []
  name_count = len(names)
  for (i,name) in enumerate(names):
    if i != 0:
      buf.append(", " if name_count > 2 else " ")
    if i == name_count-1 and name_count > 1:
      buf.append("and ")
    buf.append(add_article(name))
  return "".join(buf)

def get_noun(words, things):
  if words[0] in articles:
    if len(words) > 1:
      done = False
      for t in things:
        n = t.name.split()
        if list_prefix(n, words[1:]):
          noun = t.name
          words = words[len(n)+1:]
          done = True
          break
      if not done:
        noun = words[1]
        words = words[2:]
  else:
    done = False
    for t in things:
      n = t.name.split()
      if list_prefix(n, words):
        noun = t.name
        words = words[len(n):]
        done = True
        break
    if not done:
      noun = words[0]
      words = words[1:]
  return (noun, words)

def list_prefix(a, b):  # is a a prefix of b
  if not a:
    return True
  if not b:
    return False
  if a[0] != b[0]:
    return False
  return list_prefix(a[1:], b[1:])



