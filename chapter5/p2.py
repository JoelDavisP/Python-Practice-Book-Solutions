def readlines(fnames):
    """Reading each lines of the files and chosing lines having length > 40"""
    for fn in fnames:
        f = open(fn,'r')
        for line in f:
            if len(line) > 40:
                yield line


def printlines(lines):
    """ Printing each lines one by one"""
    for l in lines:
        print l

def main(fnames):
    """This program takes one or more filenames as arguments and prints           all the lines which are longer than 40 characters. """
    l = readlines(fnames)
    printlines(l)

main(['data.txt','data2.txt','data3.txt','data4.txt','data5.txt'])
