import time

def profile(fn):
    """It  takes a function as argument and returns a new function, 
       which behaves exactly similar to the given function, except 
       that it prints the time consumed in executing it. """
    def g(arg):
        start = time.time()
        ans = fn(arg)
        end = time.time()
        print "Time taken : " + str(end - start) + "sec"
        print "Output is: ", ans
    return g 

def fib(n):
    cache = {}
    cache[0] = 0
    cache[1] = 1
    if n in cache:
        return cache[n]
    else:
        cache[n] = fib(n-1)+ fib(n-2)
        return cache[n]

x = profile(fib)
x(10)
            
