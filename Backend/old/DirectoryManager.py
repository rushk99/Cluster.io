import os
import sys

curr_dir = os.curdir

print(curr_dir)

new_dir = "/Test01"

new_dir_path = curr_dir + new_dir

print(new_dir_path)

if os.path.isdir(new_dir_path):
    print("The directory does exist")
else:
    print("The directory doesn't exist")
    os.mkdir(new_dir_path)

exit(0)
