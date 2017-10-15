def dups(l):
    """Input a list, output all duplicated(repeating) elements in the list.     """
    l_new = []
    for i in l:
        if i not in l_new and l.count(i) > 1:
            l_new.append(i)
    return l_new

print dups([1, 1, 2, 12, 21, 25, 58, 12, 35])
