#Write a python program to get the path and name of the file that is currently executing.
class getWorkingFile:
    def __init__(self):
        pass
    def returnFilePath(self):
        return os.path.realpath(__file__)
#Driver code
if __name__ == "__main__":
    import os
    outputObject = getWorkingFile()
    print(outputObject.returnFilePath())
