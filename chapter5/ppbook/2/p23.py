import sys
def centre_align():
    """Input: filename as command line arguments. Output: All lines aligned         centre. """
    fname = sys.argv[1]
    f = open(fname, 'r')
    r = f.readlines()
    i = 0
    for l in r:
        if len(l) > i:
            i = len(l)
    for m in r:
        if len(m) < i:
            print ( (i - len(m)) / 2) * '',
        print m
    f.close()
centre_align()



