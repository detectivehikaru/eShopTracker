import urllib.request
import commands.version

try:

    github_version_url = ("https://raw.githubusercontent.com/detectivehikaru/eShopTracker/main/githubResources/version" \
                         ".txt ")

    github_data = urllib.request.urlopen(github_version_url)

except:
    print("Unable to check for updates, ensure you have an active internet connection")


def checkForUpdate():
    try:
        latest_version = ""
        for line in github_data:
            latest_version = line.decode('utf-8')

        if commands.version.version_info == latest_version:
            if commands.version.version_control == "release":
                print("You are up to date!")
            elif commands.version.version_control == "beta":
                print("This version is in " + commands.version.version_control)
            elif commands.version.version_control == "alpha":
                print("This version is in " + commands.version.version_control)
            else:
                print("This version is unidentified")
        else:
            if commands.version.version_control == "release":
                print(
                    "eShopTracker has an update! Go to https://github.com/detectivehikaru/eShopTracker/releases and download "
                    "the latest version")
            elif commands.version.version_control == "beta":
                print("This version is in " + commands.version.version_control)
            elif commands.version.version_control == "alpha":
                print("This version is in " + commands.version.version_control)
            else:
                print("This version is unidentified")

    except:
        pass
