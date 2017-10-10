import os
import sys

def lines_py():
    """It  compute the total number of lines of code in all python files 
      (.py extension) in a specified directory recursively. """
    dname = sys.argv[1]
    dpath = os.path.abspath(dname)
    line_count = 0
    for fpath,dnames,fnames in os.walk(dpath):
            for i in fnames:
                j = os.path.join(fpath,i)
                if i.split('.')[1] == 'py':
                    fn =  open(j, 'r')
                    for j in fn.readlines():
                        line_count += 1
                        yield line_count
                        
y = lines_py()
while True:
    print y.next()
