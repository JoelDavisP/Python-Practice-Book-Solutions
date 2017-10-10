import sys
import tablib

def csvtoxls():
    """It reads a csv file and exports it as Excel file. Program takes
        two command line arguments, name of csv file and Excel file resp. """
    csv = sys.argv[1]
    xls = sys.argv[2]
    data = tablib.Dataset()
    with open(csv, 'r') as f:
        data.csv = f.read()
    with open(xls, 'wb') as f:
        f.write(data.xls)

csvtoxls()
