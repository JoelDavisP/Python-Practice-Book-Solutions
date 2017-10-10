def lensort(l):
    """ This function sorts a list of strings based on their length. """
    return sorted(l, key = len)

print lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
