import sys
def head():
    """Prints head (first 10 lines) of the file. Input file name as command          line argument """
    fname = sys.argv[1]
    f = open(fname, 'r')
    for i in range(10):
       print f.next()
    f.close()
head()

