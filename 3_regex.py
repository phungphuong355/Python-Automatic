#! /usr/bin/env python3

import re

# regex basic
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])  # 12345
print(result[0])  # [12345]
print(result)  # <re.Match object; span=(39, 46), match='[12345]'>

"""
>>> grep thon /usr/share/dict/words

>>> grep -i python /usr/share/dict/words

>>> grep l.rts /usr/share/dict/words

>>> grep ^fruit /usr/share/dict/words

>>> grep cat$ /usr/share/dict/words
"""

print(re.search(r"aza", "plaza"))  # <re.Match object; span=(2, 5), match='aza'>

print(re.search(r'^x', "xenon"))  # <re.Match object; span=(0, 1), match='x'>
print(re.search(r'^x', "n xenon"))  # None


print(re.search(r'p.ng', "penguin"))  # <re.Match object; span=(0, 4), match='peng'>
print(re.search(r'p.ng', "clapping"))  # <re.Match object; span=(4, 8), match='ping'>
print(re.search(r'p.ng', "sponge"))  # <re.Match object; span=(1, 5), match='pong'>

# Wildcards and Character Classes
# [a-zA-Z0-9]
print(re.search(r'[Pp]ython', 'Python'))  # <re.Match object; span=(0, 6), match='Python'>
print(re.search(r'[a-z]way', 'The end of the highway'))  # <re.Match object; span=(18, 22), match='hway'>
print(re.search(r'[a-z]way', 'What a way to go'))  # None
print(re.search(r'cloud[a-zA-Z0-9]', 'cloudy'))  # <re.Match object; span=(0, 6), match='cloudy'>
print(re.search(r'cloud[a-zA-Z0-9]', 'cloud9'))  # <re.Match object; span=(0, 6), match='cloud9'>
# [^]
print(re.search(r'[^a-zA-Z]', "This is a sentence with space."))  # <re.Match object; span=(4, 5), match=' '>
print(re.search(r'[^a-zA-z ]', "This is a sentence with space."))  # <re.Match object; span=(29, 30), match='.'>
# |
print(re.search(r'cat|dog', "I like cats."))  # <re.Match object; span=(7, 10), match='cat'>
print(re.search(r'cat|dog', "I like dogs."))  # <re.Match object; span=(7, 10), match='dog'>
print(re.search(r'cat|dog', "I like both dogs and cats."))  # <re.Match object; span=(12, 15), match='dog'>
print(re.findall(r'cat|dog', "I like both dogs and cats."))  # ['dog', 'cat']

# Repetition Qualifiers
print(re.search(r'Py.*n', "Pygmalion"))  # <re.Match object; span=(0, 9), match='Pygmalion'>
print(re.search(r'Py.*n', "Python Programing"))  # <re.Match object; span=(0, 16), match='Python Programin'>
print(re.search(r'Py[a-z]*n', "Python Programing"))  # <re.Match object; span=(0, 6), match='Python'>
print(re.search(r'Py[a-z]*n', "Pyn"))  # <re.Match object; span=(0, 3), match='Pyn'>
# +
print(re.search(r'o+l+', 'goldfish'))  # <re.Match object; span=(1, 3), match='ol'>
print(re.search(r'o+l+', 'woolly'))  # <re.Match object; span=(1, 5), match='ooll'>
print(re.search(r'o+l+', 'boil'))  # None
# ?
print(re.search(r'p?each', "To each their own"))  # <re.Match object; span=(3, 7), match='each'>
print(re.search(r'p?each', "I like peaches"))  # <re.Match object; span=(7, 12), match='peach'>


