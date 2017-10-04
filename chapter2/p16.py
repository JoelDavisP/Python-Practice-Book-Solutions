def extsort(l):
    """Input a list of filenames, then sort the list based on extension. """
    return sorted(l, key = lambda x:x.split('.')[1])

print extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
