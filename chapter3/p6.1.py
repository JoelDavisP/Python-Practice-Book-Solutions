import os
import sys
import urllib
import re
def anti_html():
    """This function reads a url and download the html from web. Then print
     it after html tags."""

    url = sys.argv[1]
    if url[len(url) -1] == "/":
        name = "index.html"
    else:
        name1 = url.split('/')
        name = name1[len(name1) - 1]
    print "saving " + url + " as " + name
    urllib.urlretrieve(url, os.path.join
              ('/home/joel/Desktop/practice_book_problems/chapter3' + name))
    
    for f in open(('/home/joel/Desktop/practice_book_problems/chapter3' 
            + name)):
        s = re.sub(r'<.*>', '', f)
        t = re.sub(r'\s+', ' ',s)
anti_html()
