def unique(l):
    """Input a list, output all unique(not repeating) elements in the list.     """
    x = []
    for i in l:
        if i not in x:
            x.append(i)
    return x

print unique([1, 1, 2, 12, 21, 25, 58, 12, 35])
