import urllib.request
import commands.version

try:

    github_version_url = ("https://raw.githubusercontent.com/detectiveren/eShopTracker/main/githubResources/version"
                          ".txt ")  # This is the URL where the current version is stored

    github_data = urllib.request.urlopen(github_version_url)

except:
    print("Unable to check for updates, ensure you have an active internet connection")


def checkForUpdate():
    try:
        latest_version = ""
        for line in github_data:
            latest_version = line.decode('utf-8')  # Grab the version data from GitHub and decode it in utf-8

        if commands.version.version_info == latest_version:  # Check what version the program is against what the
            # GitHub version is
            if commands.version.version_control == "release":
                print("You are up to date!")
            else:
                print("This version is in " + commands.version.version_control)
        else:
            if commands.version.version_control == "release":
                print(
                    "eShopTracker has an update! Go to https://github.com/detectiveren/eShopTracker/releases and "
                    "download"
                    " the latest version")
            else:
                print("This version is in " + commands.version.version_control)

    except:
        print("This version branch is " + commands.version.version_control)
