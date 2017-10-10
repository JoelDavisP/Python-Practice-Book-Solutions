import os
import sys
path = sys.argv[1]
init = len(path.split('/')) +1
def dir_tree(path):
    """The program should take path of a directory as input and print 
      all the files in it recursively as a tree. """
    files = os.listdir(path)
    for f in sorted(files):
        fp = os.path.join(path, f)
        new = len(fp.split('/'))
        if os.path.isfile(fp):
            print (new-init)*"|  \t" +'|--'  + os.path.basename(fp)
        else:
            print (new - init)* "<<< " + os.path.basename(fp) +">>>" + "\n"
            print dir_tree(fp)

dir_tree(path)
