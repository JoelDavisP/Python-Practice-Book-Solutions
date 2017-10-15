def treemap(f, l, res = None):
    """It map a function over nested list. """
    if res is None:
        res = []
    for i in l:
        if isinstance(i, list):
            x = []
            treemap(f, i, x)
            res.append(x) 
        else:
            res.append(f(i))
    return res

print treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
