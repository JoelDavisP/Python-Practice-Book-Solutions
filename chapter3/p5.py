import os
import sys
import urllib

def web_get():
    """This function reads a url and download the url. Then save it with
        the basename of the url. If url ends with a /, make basename as
        index.html"""

    url = sys.argv[1]
    if url[len(url) -1] == "/":
        name = "index.html"
    else:
        name1 = url.split('/')
        name = name1[len(name1) - 1]
    print "saving " + url + " as " + name
    urllib.urlretrieve(url, os.path.join
              ('/home/joel/Desktop/practice_book_problems/chapter3' + name))

web_get()
