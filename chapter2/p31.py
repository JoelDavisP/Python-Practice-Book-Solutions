import sys
def parse_csv(delimit):
    """Input: a  filename as command line argument and a delimiter.
     Output: Removing all comments and spliting at the specified delimiter,      then Parsing line by line and printed. """
    fname = sys.argv[1]
    f = open(fname, 'r')
    s = f.read()
    r = s.split()
    x = []
    for l in r:
        if l[0] != '#':
            a = l.split(delimit)
            x.append(a)
    return x
    f.close()
print parse_csv('!')
