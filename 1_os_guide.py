import os
import datetime

# OS
# help(os)
# help(datetime)

# check file exist
if os.path.exists("./write_file.txt"):
    # os.rename("write_file.txt", "rename_file.txt")
    # remove file
    os.remove("./write_file.txt")

if os.path.exists("./new_dir"):
    os.rmdir("new_dir")

# Get file size
print(os.path.getsize("./rename_file.txt"))
# Get time
timestamp = os.path.getmtime("rename_file.txt")
print(datetime.date.fromtimestamp(timestamp))
# Full path file
print(os.path.abspath("./rename_file.txt"))

# Show list file in dir
print(os.listdir("./modules"))
dir_ = "../Automatic"
for name in os.listdir(dir_):
    # concatenate path and file
    fullname = os.path.join(dir_, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))

# help(os.chdir)
# command line "cd"
os.mkdir("new_dir")
os.chdir("new_dir")
os.chdir("..")
# command line "pwd"
print(os.getcwd())
