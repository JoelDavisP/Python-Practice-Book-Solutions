import urllib
import re
import sys
def links():
    """It takes a url as command line argument and print all urls linked 
       from that page."""
    url = sys.argv[1]
    web = urllib.urlopen(url)
    for i in web:
        out = re.findall(r'"http\S*"', i)
        for j in out:
           print j

links()
