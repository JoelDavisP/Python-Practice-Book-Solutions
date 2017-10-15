def treerev(l, res = None):
    """It reverse elements of a nested-list recursively. """
    if res is None:
        res = []
    for i in l:
        if isinstance(i, list):
            res.insert(0, treerev(i, None)) 
        else:
            res.insert(0, i)
    return res

print treerev([[1, 2], [3, [4, 5]], 6])
