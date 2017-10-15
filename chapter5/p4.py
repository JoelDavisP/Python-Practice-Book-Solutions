import os
import sys

def num_py():
    """It  compute the number of python files (.py extension) in a specified    directory recursively. """
    dname = sys.argv[1]
    dpath = os.path.abspath(dname)
    count = 0
    for fpath,dnames,fnames in os.walk(dpath):
            for i in fnames:
                if i.split('.')[1] == 'py':
                    count += 1
                    yield os.path.join(fpath, i), count
                        
y = num_py()
while True:
    print y.next()
