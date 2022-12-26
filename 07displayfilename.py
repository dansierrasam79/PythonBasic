'''Write a Python program to accept a filename from the user and print the extension of that.
Sample filename : abc.java
Output : java'''

class displayExtensionName:
    def __init__(self, fileName):
        self.fName = fileName
    def extractFilename(self):
        fileList = self.fName.split(".")
        return fileList[1]
#Driver code
if __name__ == "__main__":
    userInput = input("Enter the filename along with the extension: ")
    outputObject = displayExtensionName(userInput)
    print("The file extension is: ", outputObject.extractFilename())
