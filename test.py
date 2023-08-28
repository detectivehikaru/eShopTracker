from nintendeals import noa, noe, noj
from commands import printallregions, listallregions, welcome, version, notifications


def runTest():
    printallregions.printAllRegions()
    listallregions.listAllRegions()
    welcome.welcomeMessage()
    version.displayVersion()
    notifications.checkForUpdate()


runTest()
