import os
import sys

if sys.argv[1] == "list_dir":
    if len(sys.argv) < 3:
        print("Not enough parameters to execute command")
        print("Usage: list_dir <dir>")
    elif len(sys.argv) > 3:
        print("Too many parameters to execute command")
        print("Usage: list_dir <dir>")
    else:
        os.system("dir {}".format(sys.argv[2]))

if sys.argv[1] == "move_dir":
    if len(sys.argv) < 4:
        print("Not enough parameters to execute command")
        print("Usage: move_dir <dir1> <dir2>")
    elif len(sys.argv) > 4:
        print("Too many parameters to execute command")
        print("Usage: move_dir <dir1> <dir2>")
    else:
        os.system("move {} {}".format(sys.argv[2], sys.argv[3]))