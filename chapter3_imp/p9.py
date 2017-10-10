import re

def valid_phone(st):
    """ This function reads a string as an input which is a number and 
        prints whether it is a valid one or not"""

    if len(st) == 10:
        if re.match(r'^[\d]{10}$', st):
            print "Valid number.."
    else:
        print "Invalid number.."

valid_phone("9495096858")
valid_phone("94950945758")
