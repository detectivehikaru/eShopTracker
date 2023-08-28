from nintendeals import noa, noe, noj
import printallregions
import listallregions
import welcome
import version
import notifications


def runTest():
    printallregions.printAllRegions()
    listallregions.listAllRegions()
    welcome.welcomeMessage()
    version.displayVersion()
    notifications.checkForUpdate()


runTest()
