def anagrams(l):
    """Input a list of strings. Output a list of Anagrams.
     Two words are called anagrams if one word can be formed 
     by rearranging letters of another. """
    lnew = []
    for i in l:
        for j in l:
            if len(i) == len(j) and equal(i,j):
                lnew.append((i,j))
    print lnew

def equal(s1,s2):
    """Input two strings. Return True, if both have same letters."""    
    fl = 0
    for l in s1:
        if s1 != s2 and l in s2:
            fl += 1
    return fl == len(s1) 

anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])       
