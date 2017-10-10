def unique_new(l, key = None):
    """Input a list, output all unique(not repeating) elements in the list.
       It takes an optional key function as argument and use the return            value of the key function to check for uniqueness.     """
    l_new = []
    for i in l:
        l_new.append(key(i))
    return list(set(l_new))

print unique_new(["python", "java", "Python", "Java"], key=lambda s: s.lower())
