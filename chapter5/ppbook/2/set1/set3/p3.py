def sum_strg(l):
    """Prints the concatenated string if you give a list of strings as input     """
    s = ""
    for words in l:
        for letters in words:
            s += letters
    return s
print sum_strg(["aa", "bb", "cc"])
print sum_strg(["hell","owo","rld"])
