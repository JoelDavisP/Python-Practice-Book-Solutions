def square(x):
    return x*x

def map_list_comp(fn,ls):
    """It applies a function to each element of a list. Input function name     and a list. output function applied to each element of list. """
    print [fn(x) for x in ls]
map_list_comp(square, range(5))
