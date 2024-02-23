import commands.settings

version = "1.9.0"
version_message = "Version " + version
version_info = "version=" + version
version_control = "alpha"


def displayVersion():
    if commands.settings.version:
        print(version_message)


def displayVersionBranch():
    if commands.settings.version:
        print(version_control)


def displayVersionDetails():
    if commands.settings.version:
        print(version_message + "-" + version_control)
