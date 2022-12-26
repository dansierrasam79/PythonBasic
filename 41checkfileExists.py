#Write a Python program to check whether a file exists.
class fileExists:
    def __init__(self,fName):
        self.fileName = fName
    def checkFile(self):
        return os.path.isfile(self.fileName)
#Driver code
if __name__ == "__main__":
    import os
    path = input("Enter the file path: ")
    outputObject = fileExists(path)
    if outputObject.checkFile() == True:
        print("File exists")
    else:
        print("File does NOT exist")
