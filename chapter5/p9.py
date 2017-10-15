def my_enum(it):
    """It  takes an iteratable and returns an iterator over pairs 
      (index, value) for each value in the source. """
    l = []
    i = 0
    try:
        while True:
            x = it.next()
            l.append((i, x))
            i += 1
    except StopIteration:
        pass
    return l

it1 = iter(["a", "b", "c", "d", "e"])
print my_enum(it1)
