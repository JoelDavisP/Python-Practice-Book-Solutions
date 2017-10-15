def prod_ls(l):
    """Prints the product of a given list of numbers """
    s = 1
    for i in l:
        s *= i
    return s

def fact(n):
    """Prints the factorial of a given number """
    a = range(1, n+1)
    return prod_ls(a)

print fact(5)
