import sys
def reverse_lines():
    """It reverses the lines of a file. Input filename as command line 
        argument"""
    fname = sys.argv[1]
    f = open(fname, 'r')
    for i in f:
        x = list(i)
        print ''.join(x[::-1]) 
    f.close()
reverse_lines()
