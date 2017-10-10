import sys

def splitn():
    """It takes an integer 'n' and a 'filename' as command line arguments 
       and splits the file into multiple small files with each having n 
       lines. """
    fno = 0
    n = sys.argv[1]
    num = int(n)
    fname = sys.argv[2]
    new = open(fname.split('.')[0] + '_' + str(fno) + '.txt', 'a')
    f = open(fname,'r')
    i = 0
    for ln in f.readlines():
        if i == num:
            fno += 1
            new = open(fname.split('.')[0] + '_' + str(fno) + '.txt', 'a')
            i = 0    
        new.write(ln)
        i += 1
splitn()        
