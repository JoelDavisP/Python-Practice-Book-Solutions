def sum_ls(l):
    """Prints the sum of a given list of numbers """
    s = 0
    for i in l:
        s+=i
    return s
print sum_ls([1, 2, 3, 4, 5, 6])
print sum_ls([1.21, 2.34, 3.456, 4.4893, 5.120, 6])
