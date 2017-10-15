def vectorize(fn):
    """It takes a function f and return a new function, which takes a list 
    as argument and calls f for every element and returns the result as a 
    list. """
    def g(l):
        lnew = []
        for i in l:
            lnew.append(fn(i))
        print lnew
    return g
        
def square(x):
    return x*x

f = vectorize(square)
f([1, 2, 3])
h = vectorize(len)
h(["hello", "world"])
h([[1, 2], [2, 3, 4]])
