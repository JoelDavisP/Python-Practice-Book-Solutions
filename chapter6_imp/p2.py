def flatten_dict(a, b = None, res = None):
    """It flatten a nested dictionary by joining the keys with '.' 
       character. """
    if res == None:
        res = {}

    for x,y in a.items():
        if isinstance(y, dict):
            flatten_dict(y, x, res)
        else:
            if b is None:
                res[x] = y
            else:
                res[b + '.' + x] = y

    return res

print flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
