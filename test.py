from nintendeals import noa, noe, noj
from commands import printallregions, listallregions, welcome, version, notifications, listcommands


def runTest():
    printallregions.printAllRegions()
    listallregions.listAllRegions()
    welcome.welcomeMessage()
    version.displayVersion()
    notifications.checkForUpdate()
    listcommands.commands()
    listcommands.detailedCommands()


runTest()
