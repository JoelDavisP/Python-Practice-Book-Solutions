def my_zip(it1, it2):
    """It  take two iteratables and returns a list zipped over pairs 
      (it1, it2) for each value in the iterators. """
    l = []
    try:
        while True:
            x = it1.next()
            y = it2.next()
            l.append((x, y))
    except StopIteration:
        pass
    return l

it1 = iter(["a", "b", "c", "d", "e"])
it2 = iter([1,2,3,4,5])
print my_zip(it1, it2)
