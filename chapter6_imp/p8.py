def count_change(amnt, l):
    """It counts the number of ways to change any given amount. Available 
      coins are also passed as argument to the function. """
    if amnt == 0:
        return 1 
    if amnt < 0 or len(l) == 0:
        return 0
    else:
        return count_change(amnt, l[1:]) + count_change(amnt - l[0], l)

print count_change(10, [5])
print count_change(10, [1, 2])
print count_change(100, [1, 5, 10, 25, 50])
