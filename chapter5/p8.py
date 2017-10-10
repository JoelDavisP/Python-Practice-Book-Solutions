import itertools

def peep(it):
    """It takes an iterator as argument and returns the first element and an     equivalant iterator. """
    a = it.next()
    l = []
    l.append(a)
    try:
        while True:
            x = it.next()
            l.append(x)
    except StopIteration:
        pass 
    return a,l
it1 = iter(range(5))
print peep(it1)
