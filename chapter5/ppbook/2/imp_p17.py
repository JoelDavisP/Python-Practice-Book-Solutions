import sys
def reverse_file():
    """It prints lines of a file in reverse order.Input 
        filename as commandline argument."""
    fname = sys.argv[1]
    f = open(fname, 'r')
    for i in reversed(f.readlines()):
        print i
    f.close()

reverse_file()
