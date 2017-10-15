def prod_rec(n1,n2):
    """This function will multiply 2 numbers recursively using + and - 
       operators only. """
    if n1 == 0 or n2 == 0:
        return 0
    if n1 == 1:
        return n2
    if n2 == 1:
        return n1
    else:
        return n1 + prod_rec(n1, n2 - 1)

print prod_rec(0, 1)
print prod_rec(1, 10)
print prod_rec(5, 3)
print prod_rec(4, 10)
