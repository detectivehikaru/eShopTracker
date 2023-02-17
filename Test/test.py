from nintendeals import noa, noe, noj
from commands import printallregions, listallregions
import sys


sys.path.insert(0, '/commands')

def runTest():
    printallregions.printAllRegions()
    listallregions.listAllRegions()

runTest()