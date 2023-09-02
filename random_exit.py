#! /usr/bin/env python

import sys
import random

value = random.randint(0, 3)
print("Returning: {}".format(value))
sys.exit(value)
