def rev(l):
    """This function outputs a reversed list if you input a list"""
    l_new = []
    for i in range(len(l)-1, -1, -1):
        l_new.append(l[i])
    return l_new
print rev([1, 2, 3, 4, 5, 6])
