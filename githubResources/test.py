from nintendeals import noa, noe, noj
import sys
sys.path.append('../commands')
import commands.printallregions
import commands.listallregions
import commands.welcome
import commands.version
import commands.notifications


def runTest():
    commands.printallregions.printAllRegions()
    commands.listallregions.listAllRegions()
    commands.welcome.welcomeMessage()
    commands.version.displayVersion()
    commands.notifications.checkForUpdate()


runTest()
