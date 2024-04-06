# Activate Commands
listallregions = True
listcommands = True
notifications = True
online = True
printallregions = True
region = True
save = True
search = True
info = True
version = True
welcome = True
debug = False

# Detailed Parameters for Commands
notifications_url = "https://raw.githubusercontent.com/detectiveren/eShopTracker/main/githubResources/version.txt"
saveAuto = 0

if debug:
    listallregions = True
    listcommands = True
    notifications = True
    online = True
    printallregions = True
    region = True
    save = True
    search = True
    info = True
    version = True
    welcome = True


def printListAllRegions():
    if listallregions:
        print("listallregions: Enabled")
    else:
        print("listallregions: Disabled")


def printlistCommands():
    if listcommands:
        print("listcommands: Enabled")
    else:
        print("listcommands: Disabled")


def printNotifications():
    if notifications:
        print("notifications: Enabled")
    else:
        print("notifications: Disabled")


def printOnline():
    if online:
        print("online: Enabled")
    else:
        print("online: Disabled")


def printAllRegionsCommand():
    if printallregions:
        print("printallregions: Enabled")
    else:
        print("printallregions: Disabled")


def printRegion():
    if region:
        print("region: Enabled")
    else:
        print("region: Disabled")


def printSave():
    if save:
        print("save: Enabled")
    else:
        print("save: Disabled")


def printSearch():
    if search:
        print("search: Enabled")
    else:
        print("search: Disabled")


def printInfo():
    if info:
        print("info: Enabled")
    else:
        print("info: Disabled")


def printVersion():
    if version:
        print("version: Enabled")
    else:
        print("version: Disabled")


def printWelcome():
    if welcome:
        print("welcome: Enabled")
    else:
        print("welcome: Disabled")


def printDebug():
    if debug:
        print("debug: Enabled")
    else:
        print("debug: Disabled")


def printSettings():
    printListAllRegions()
    printlistCommands()
    printNotifications()
    printOnline()
    printAllRegionsCommand()
    printRegion()
    printSave()
    printSearch()
    printInfo()
    printVersion()
    printWelcome()
    printDebug()
