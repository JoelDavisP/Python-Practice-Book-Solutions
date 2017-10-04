import sys
def wrap():
    """Input: filename and width as command line arguments. Output: All lines
        longer than width are wrapped. """
    fname = sys.argv[1]
    width = sys.argv[2]
    f = open(fname, 'r')
    r = f.readlines()
    for l in r:
        if len(l) > width:
            print l
      #      x = list(l)
       #     x1 =x[:width]  
        #    print ''.join(x1)
            #print ''.join(x2)
    f.close()
wrap()
