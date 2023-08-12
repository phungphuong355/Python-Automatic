# Open file
hello = open("./hello.txt")
print(hello.readline())
print(hello.read())
hello.close()

# Read file
with open("./hello.txt") as file:
    print(file.read())

with open("./hello.txt") as file:
    for line in file:
        print(line.strip().upper())

file = open("./hello.txt")
lines = file.readlines()
file.close()
print(lines)

"""
--------------------------------------------------------------------------
| 'r'  | open for reading (default)                                      |
--------------------------------------------------------------------------
| 'w'  | open for writing, truncating the file fist                      |
--------------------------------------------------------------------------
| 'x'  | open for exclusive creation, failing if the file already exists |
--------------------------------------------------------------------------
| 'a'  | open for writing appending to the end of file if it exists      | 
--------------------------------------------------------------------------
| 'b'  | binary mode                                                     |
--------------------------------------------------------------------------
| 't'  | text mode (default)                                             |
--------------------------------------------------------------------------
| '+'  | open for updating (reading and writing)                         |
--------------------------------------------------------------------------
"""

# Write file
with open(file="./write_file.txt", mode="w") as file:
    file.write("I am Home\nI give you comfort\n")
