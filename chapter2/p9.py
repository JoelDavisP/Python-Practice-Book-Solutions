def cumulative_prod(l):
    """Prints the cumulative sum of a list of numbers: eg: input [a, b, c]        output will be [a, a*b, a*b*c]. """
    l_new = []
    for i in l:
        if isinstance(i, int) or isinstance(i, float):
            l_new.append(i * prod(l[0 : l.index(i)]))
    return l_new

def prod(l):
    """Prints the product of all elements in the list"""
    p = 1
    for i in l:
        p *= i
    return p

print cumulative_prod([4, 3, 2, 1])
