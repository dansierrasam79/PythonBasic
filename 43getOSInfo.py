#Write a Python program to get OS name, platform and release information.
class getOSInfo:
    def __init__(self):
        pass
    def getOSInformation(self):
        return os.name, sys.platform, sys.version_info
#Driver code
if __name__ == "__main__":
    import os, sys
    outputObject = getOSInfo()
    print(outputObject.getOSInformation())
