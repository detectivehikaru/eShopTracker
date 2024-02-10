from commands import (printallregions, listallregions, welcome, region, listcommands, search, notifications, version, online)

if online.internetStatus():
    connection = True
else:
    connection = False


def overwriteFile(file):
    with open(file, 'w', encoding="utf-8") as f:
        clean = ""
        f.write(clean)
        f.close()


def runCommands(command, internetConnection):
    command = str.lower(command)
    if command == "printallregions":
        if internetConnection:
            printallregions.printAllRegions()
        else:
            print("You are not connected online")
    elif command == "listallregions":
        if internetConnection:
            listallregions.listAllRegions()
        else:
            print("You are not connected online")
    elif command == "welcome":
        welcome.welcomeMessage()
    elif command in ["region", "region -noa", "region -noe", "region -noj", "region -p -noa", "region -p -noe",
                     "region -p -noj"]:
        if internetConnection:
            region.region(command)
        else:
            print("You are not connected online")
    elif command == "search":
        if internetConnection:
            search.search()
        else:
            print("You are not connected online")
    elif command == "version":
        version.displayVersion()
    elif command == "commands":
        listcommands.commands()
    elif command == "commands -p":
        listcommands.detailedCommands()
    elif command == "version branch":
        version.displayVersionBranch()
    elif command == "version details":
        version.displayVersionDetails()
    elif command == "overwrite":
        command = input("Enter the text file you would like to overwrite (include file extension): ")
        overwriteFile(command)
    else:
        print("Command Not Found")


def main():
    end = 0
    welcome.welcomeMessage()
    notifications.checkForUpdate()
    online.displayInternetStatus()
    while end == 0:
        cmd = input("eShopTracker > ")
        runCommands(cmd, connection)


main()

