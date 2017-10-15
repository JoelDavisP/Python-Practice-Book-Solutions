def minimum(l):
    """Prints the minimum value of a given list"""
    mini = l[0]
    for i in l:
        if i < mini:
            mini = i
    return mini

def maximum(l):
    """Prints the maximum value of a given list"""
    maxi = l[0]
    for i in l:
        if i > maxi:
            maxi = i
    return maxi

print minimum(["hello", "good", "morning", "young", "man"]) #prints the                                     first word comes in the alphabetical order 
print maximum(["hello", "good", "morning", "young", "man"]) #prints thr last                                        word comes in the alphabetical order

print minimum([145, 562, 23, 87, 7, 95])
print maximum([112, 234, 34, 7, 5, 6])
