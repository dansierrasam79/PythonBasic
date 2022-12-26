# Write a Python program to get the Python version you are using.

class getPythonVersion:
    def __init__(self):
    # No arguments to pass through
        pass
    def getPyVersion(self):
        print("The current Python version: " , sys.version[0:5])
#Driver code
if __name__ == "__main__":
    import sys
    outputObject = getPythonVersion()
    outputObject.getPyVersion()
