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

# Escaping Characters
# \
print(re.search(r'\.com', 'welcome'))  # None
print(re.search(r'\.com', 'domain.com'))  # <re.Match object; span=(8, 12), match='.com'>
# \w \d \s \b
print(re.search(r'\w*', 'This is an example'))  # <re.Match object; span=(0, 4), match='This'>
print(re.search(r'\w*', 'And_this_is_another'))  # <re.Match object; span=(0, 19), match='And_this_is_another'>

# Regular Expressions in Action
print(re.search(r'A.*a', "Azerbaijan"))  # <re.Match object; span=(0, 9), match='Azerbaija'>
print(re.search(r'^A.*a$', "Azerbaijan"))  # None
print(re.search(r'^A.*a$', "Australia"))  # <re.Match object; span=(0, 9), match='Australia'>
pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
print(re.search(pattern, '_this_is_a_valid_variable_name'))
# <re.Match object; span=(0, 30), match='_this_is_a_valid_variable_name'>
print(re.search(pattern, "this isn't a valid a variable"))  # None
print(re.search(pattern, 'my_variable1'))
# <re.Match object; span=(0, 12), match='my_variable1'>
print(re.search(pattern, '2my_variable1'))  # None


# Capturing Groups
def rearrange_name(name):
    result = re.search(r"^([\w .-]*), ([\w \.-]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])


name = rearrange_name("Kennedy, John F.")
print(name)

# More on Repetition Qualifiers
print(re.search(r"[a-zA-Z]{5}", "a ghost"))  # <re.Match object; span=(2, 7), match='ghost'>
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))  # <re.Match object; span=(2, 7), match='scary'>
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))  # ['scary', 'ghost', 'appea']
print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared"))  # ['scary', 'ghost']
print(re.findall(r"\w{5,10}", "I really like strawberries"))  # ['really', 'strawberri']
print(re.findall(r"\b\w{5,10}\b", "I really like strawberries"))  # ['really']
print(re.findall(r"\w{5,}", "I really like strawberries"))  # ['really', 'strawberries']
print(re.findall(r"\w{,20}", "I really like strawberries"))  # ['I', '', 'really', '', 'like', '', 'strawberries', '']
print(re.findall(r"s\w{,20}", "I really like strawberries"))  # ['strawberries']


# Extracting a PID Using regexes in Python
def extract_pid(log_line):
    regex = r"\[(\d+)\]: ([A-Z]\w*)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])


print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"))  # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]"))  # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message"))  # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup"))  # 67890 (RUNNING)

# Splitting and Replacing
print(re.split(r'[.?!]', "One sentence. Another one? And the last one!"))
# ['One sentence', ' Another one', ' And the last one', '']
print(re.split(r'([.?!])', "One sentence. Another one? And the last one!"))
# ['One sentence', '.', ' Another one', '?', ' And the last one', '!', '']
print(re.sub(r'[\w.%+-]+@[\w.-]+', "[READACTED]", "Received an email for go_nuts95@my.example.com"))
# Received an email for [READACTED]
print(re.sub(r'^([\w .-]*), ([\w .-]*)$', r'\2 \1', 'Lovelace, Ada'))
# Ada Lovelace
