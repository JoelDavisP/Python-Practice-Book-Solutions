def prod_ls(l):
    """Prints the product of a given list of numbers """
    s = 1
    for i in l:
        s *= i
    return s

print prod_ls([1.21, 2.34, 3.456, 4.4893, 5.120, 6])
