import os
import sys
"""      Program to list all the files in the given directory along with their length and last modification time."""

path = sys.argv[1]
dirs = os.listdir(path)
for i in dirs:
    path_n = path + "/%s" %(i)
    s = os.stat(path)
    print i +  "\t" + str(s.st_size) + "\t" + str(s.st_mtime)
