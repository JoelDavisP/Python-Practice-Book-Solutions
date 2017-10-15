def even(x):
    return x%2 == 0

def filter_list_comp(fn,ls):
    """It applies a function to each element of a list and returns items of
      the list for which fn(item) is True. Input function name and a list.
     output values of list after function applied to be True. """
    print [x for x in ls if fn(x)]
filter_list_comp(even, range(15))
