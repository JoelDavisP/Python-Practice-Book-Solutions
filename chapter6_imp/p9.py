def permute(l):
    """This function is used to compute all possible permutations of 
       elements of a given list. """
    ls = []
    if len(l) == 0:
        return []
    if len(l) == 1:
        return l
    else:
        for i in l:
            rest = [x for x in l if x != i]
            lnew = permute(rest)
            for j in lnew:
                ls.append([i] + [j])
        return ls

print permute([1,2,3])
