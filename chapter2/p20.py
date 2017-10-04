import sys
def grep():
    """It takes a string and a file as arguments and prints all lines     in the file which contain the specified string. Input string and     filename as command line arguments"""
    fname = sys.argv[1]
    string = sys.argv[2]
    f = open(fname, 'r')
    r = f.readlines()
    for l in r:
        if string in l:
            print l
    f.close()
grep()
