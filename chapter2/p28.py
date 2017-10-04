def enum(l):
    """This function takes a list and returns a list of tuples 
    containing (index,item) for each item in the list. """
    print [(i,l[i]) for i in range(len(l))]

enum(["a", "b", "c"])
