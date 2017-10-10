import sys
import zipfile
import os

def zipfls():
    """It take name of zip file as first argument and files to add as rest 
      of the arguments. Then produces a zipfile in that name. """
    name = sys.argv[1]
    files = sys.argv[2:]
    if name.split('.')[1] == 'zip':
        zf = zipfile.ZipFile(name, 'w', zipfile.ZIP_DEFLATED) #ZIP_DEFLATED is            the numeric constant for the usual ZIP compression method.
        for f in files:
            zf.write(f, arcname = f)
        for i in zf.namelist():
            print i
    else:
        print "Invalid filename.."

zipfls()
