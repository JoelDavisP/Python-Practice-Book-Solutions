import sys
def parse_csv():
    """Input: a C.S.V.(comma separated values) filename as command line 
    argument. Output: Parsing line by line and printed. """
    fname = sys.argv[1]
    f = open(fname, 'r')
    s = f.read()
    r = s.split()
    x = []
    for l in r:
        a = l.split(',')
        x.append(a)
    return x
    f.close()
print parse_csv()
