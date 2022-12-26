#Write a python program to call an external command in Python.
class cmdExecute:
    def __init__(self, givenString):
        self.myString = givenString
    def executeCommand(self):
        return os.system('cmd /k' + self.myString)
#Driver code
if __name__ == "__main__":
    import os
    givenString = input("Enter the command: ")
    outputObject = cmdExecute(givenString)
    outputObject.executeCommand()
