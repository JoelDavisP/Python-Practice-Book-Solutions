def valuesort(dic):
    """Input a dictionary, outputsorted list of values based on key"""
    lis = []
    for x,y in sorted(dic.items(), key = lambda x: x[0]):
        lis.append(y)
    return lis

print valuesort({'r' : 45, 'g' : 41, 'd' : 12, 'w' : 57, 'e' : 74 })
        
