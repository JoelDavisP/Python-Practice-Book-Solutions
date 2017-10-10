import urllib
import json

def myip():
    """This prints the external IP address of a machine using json module """
    url = urllib.urlopen('http://httpbin.org/get').read()
    ans = json.loads(url)
    print ans['origin']
myip()
