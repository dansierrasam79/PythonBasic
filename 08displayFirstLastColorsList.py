'''Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]'''

class displayColors:
    def __init__(self,myList):
        self.thisList = myList
    def displayfirstLastcolors(self):
        print(self.thisList[0])
        print(self.thisList[-1])
#Driver code
if __name__ == "__main__":
    myList = ["Red", "Green", "White", "Black"]
    outputObject = displayColors(myList)
    outputObject.displayfirstLastcolors()
