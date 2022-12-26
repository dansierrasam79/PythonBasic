#Write a Python program to list all files in a directory in Python.
# Folder Path: C:\Users\Programming\Desktop\Python
class returnDirFiles:
    def __init__(self, fPath):
        self.filePath = fPath
    def returnfDir(self):
        return os.listdir(self.filePath)
#Driver code
if __name__ == "__main__":
    import os
    givenPath = input("Enter the file path: ")
    outputObject = returnDirFiles(givenPath)
    print("Files in directory: ", outputObject.returnfDir())
