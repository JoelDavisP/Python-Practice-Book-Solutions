import re

def makeslug(st):
    """This will read a string as input and spaces and special charectors
       are replaced by a hyphen. More than one hyphwns and hyphen at the 
       beginning are not allowed. """
    
    
    out1 = re.sub(r'\W', '-',st)
    out2 = re.sub(r'-(-+)', '-', out1)
    if out2[0] == "-":
        return out2[1 : ]
    if out2[len(out2) -1] == "-":
        return out2[: -1]
    else:    
        return out2


