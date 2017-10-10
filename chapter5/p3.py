import os
import sys

def findfiles():
    """This function recursively descends the directory tree for the 
    specified directory and generates paths of all the files in the tree. """
    fname = sys.argv[1]
    fpath = os.path.abspath(fname)
    for path,dnames,fnames in os.walk(fpath):
        for f in fnames:
            yield os.path.join(path,f)

y = findfiles() 
while True:
    print y.next()
