def cumulative_sum(l):
    """Prints the cumulative sum of a list: eg: input [a, b, c] output 
       will be [a, a+b, a+b+c].You can input either a list of integers, or
       a list of strings. Do not mix the types. """
    l_new = []
    for i in l:
        if isinstance(i, int) or isinstance(i, float):
            l_new.append(i + sum(l[0 : l.index(i)]))
        else:
            l_new.append(l[0: l.index(i)+1])
    return l_new

print cumulative_sum([4, 3, 2, 1])
print cumulative_sum(["hai", "good", "morning"])
