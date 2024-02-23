listallregions = True
listcommands = True
notifications = True
online = True
printallregions = True
region = True
save = True
search = True
version = True
welcome = True
debug = False

if debug:
    listallregions = True
    listcommands = True
    notifications = True
    online = True
    printallregions = True
    region = True
    save = True
    search = True
    version = True
    welcome = True


def printListAllRegions():
    if listallregions == True:
        print("listallregions: Enabled")
    else:
        print("listallregions: Disabled")


def printlistCommands():
    if listcommands == True:
        print("listcommands: Enabled")
    else:
        print("listcommands: Disabled")


def printNotifications():
    if notifications == True:
        print("notifications: Enabled")
    else:
        print("notifications: Disabled")


def printOnline():
    if online == True:
        print("online: Enabled")
    else:
        print("online: Disabled")


def printAllRegionsCommand():
    if printallregions == True:
        print("printallregions: Enabled")
    else:
        print("printallregions: Disabled")


def printRegion():
    if region == True:
        print("region: Enabled")
    else:
        print("region: Disabled")


def printSave():
    if save == True:
        print("save: Enabled")
    else:
        print("save: Disabled")


def printSearch():
    if search == True:
        print("search: Enabled")
    else:
        print("search: Disabled")


def printVersion():
    if version == True:
        print("version: Enabled")
    else:
        print("version: Disabled")


def printWelcome():
    if welcome == True:
        print("welcome: Enabled")
    else:
        print("welcome: Disabled")


def printDebug():
    if debug == True:
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
    printVersion()
    printWelcome()
    printDebug()

