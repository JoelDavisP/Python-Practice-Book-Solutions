import inspect
import sys

def mydoc():
    """It takse a module name as command line argument argument and print 
        documentation for the module and each of the functions defined 
        in that module. """ 
    mod_name = sys.argv[1]
    mod = __import__(mod_name)
    print "Help on module ", mod_name
    print "\n DESCRIPTION \n"
    print mod.__doc__
    print "\n FUNCTIONS \n"
    fns = dir(mod)
    for i in fns:
        inew = getattr(mod, i)
        if inspect.isfunction(inew):
            print "\n",i + "()"

mydoc() 
