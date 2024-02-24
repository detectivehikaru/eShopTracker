from nintendeals import noa, noe, noj
from commands import (printallregions, listallregions, welcome, version, notifications, listcommands, settings,
                      search, online)


def runTest():
    printallregions.printAllRegions()
    listallregions.listAllRegions()
    welcome.welcomeMessage()
    version.displayVersion()
    notifications.checkForUpdate()
    listcommands.listBasicCommands()
    listcommands.detailedCommands()
    settings.printSettings()
    search.searchedItem("Zelda")
    search.regionSearchItem("Zelda", "NA")
    online.internetStatus()
    online.displayInternetStatus()



runTest()
