import os
"""  Program to list all files in the given directory. """
a= input("\nenter the path enclosed in double quotes\n")
dirs = os.listdir(a)
for i in dirs:
    print i
