#! /usr/bin/env python3

import re

# regex basic
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])
print(result[0])
print(result)

"""
>>> grep thon /usr/share/dict/words

>>> grep -i python /usr/share/dict/words

>>> grep l.rts /usr/share/dict/words

>>> grep ^fruit /usr/share/dict/words

>>> grep cat$ /usr/share/dict/words
"""
