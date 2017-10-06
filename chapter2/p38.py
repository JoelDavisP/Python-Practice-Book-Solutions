def invert_dict(dic):
    """Input a dictionary. Output a dictionary whose keys and values    are interchanged """
    new_dict = {}
    for i,j in dic.items():
        new_dict[j] = i
    print new_dict
invert_dict({'x': 1, 'y': 2, 'z': 3})
