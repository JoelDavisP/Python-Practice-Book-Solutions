import sys
def pos_of_space(line, width):
    """ Return the nearest location of space from width"""
    i = width
    while i != 1:
        if line[i] == " ":
            break
        i -= 1
    return i

def wrap_new():
    """Input: filename and width as command line arguments. Output: All lines    longer than width are wrapped without breaking the words. """
    fname = sys.argv[1]
    arg = sys.argv[2]
    width = int(arg)
    f = open(fname, 'r')
    r = f.readlines()
    for l in r:
        if len(l) > width:
            loc = pos_of_space(l,width)
            x = list(l)
            x1 = x[ : loc]  
            x2 = x[loc+1 :]
            print ''.join(x1)
            print ''.join(x2)
    f.close()
wrap_new()



