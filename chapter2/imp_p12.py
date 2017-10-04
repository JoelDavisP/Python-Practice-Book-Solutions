def group(l,size):
    """It  take a list and size as input, and splits the list into smaller 
    lists of given size."""

    l_new = [l[i : i+size] for i in range(0, len(l), size)]
    return l_new


print group([1,2,3,4,5,6,7,8,9],3)
