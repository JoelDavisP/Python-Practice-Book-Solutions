def two_d_array(i,j):
    """This function reads two dimensions as arguments and creates a two
       dimensional array with each element initialized to None """
    a = [[None for x in range(i)] for y in range(j)]
    a[0][0] = 5    
    print a

two_d_array(3,3)

