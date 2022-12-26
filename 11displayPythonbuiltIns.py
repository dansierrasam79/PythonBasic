'''Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.'''

class describeFunction:
    def __init__(self,helpString):
        self.helpName = helpString
    def displayDescription(self):
        print(help(self.helpName))
#Driver code
if __name__ == "__main__":
    helpStr = input("Enter the built-in function name: ")
    outputObject = describeFunction(helpStr)
    outputObject.displayDescription()
