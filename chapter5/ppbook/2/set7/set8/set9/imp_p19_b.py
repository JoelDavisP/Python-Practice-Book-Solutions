import sys
def tail():
    """Prints tail (last 10 lines) of the file. Input file name as command          line argument """
    fname = sys.argv[1]
    f = open(fname, 'r')
    r = f.readlines()
    for i in range(len(r)-1, len(r)-11, -1):
        print r[i] 
    f.close()
tail()

