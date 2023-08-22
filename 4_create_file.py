#! /usr/bin/env python
import os
import sys

filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write("New file create\n")
else:
    print("Error, the file {} already exists!".format(filename))
    sys.exit(1)
