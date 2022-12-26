#Write a Python program to locate Python site-packages.
class getPythonSitePackages:
    def __init__(self):
        pass
    def displayPythonSitePackages(self):
        return site.getsitepackages()
#Driver code
if __name__ == "__main__":
    import site
    outputObject = getPythonSitePackages()
    print("Site packages: ", outputObject.displayPythonSitePackages())
