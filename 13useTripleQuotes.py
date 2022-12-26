'''Write a Python program to print the following document.
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example'''

class docString:
    def __init__(self, textString):
        self.givenString = textString
    def displayString (self):
        print (self.givenString)
#Driver code
if __name__ == "__main__":
    text = """This is a .......
            multi-line heredoc string
            --------> example"""
    outputObject = docString (text)
    outputObject.displayString()
