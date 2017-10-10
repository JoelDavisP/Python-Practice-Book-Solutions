def zip_list_comp(l1,l2):
    """Input two lists and output a list which zips two lists using list 
        comprehension. """
    print [(l1[x], l2[y]) for x in range(len(l1)) for y in range(len(l2)) 
        if x == y ]

zip_list_comp([1, 2, 3], ["a", "b", "c"])
