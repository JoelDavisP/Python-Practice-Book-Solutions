def triplets(n):
    """Input a number, n output a list of triplets such that sum of first 
       two elements of the triplet equals the third element using numbers 
       below n """

    print [(a,b,c) for a in range(1,n) for b in range(a,n) for c in 
        range(b,n)if c == a+b]

triplets(5)
