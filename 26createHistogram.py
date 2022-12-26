#Write a Python program to create a histogram from a given list of integers.
class createHistogram:
    def __init__(self, givenList):
        self.theList = givenList
    def displayHistogram (self):
        for value in self.theList:
            oneBarValue = "*"*value
            print(oneBarValue)
#Driver code
if __name__ == "__main__":
    aList = [3,5,1,2,4]
    outputObject = createHistogram(aList)
    outputObject.displayHistogram()
