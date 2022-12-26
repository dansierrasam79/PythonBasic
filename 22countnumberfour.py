#Write a Python program to count the number 4 in a given list.
class findNumber:
    def __init__(self, givenList):
        self.numberList = givenList
    def findNumbr (self):
        for number in self.numberList:
            if number == 4:
                return True
        return False
#Driver code
if __name__ == "__main__":
    myList = [1,2,3,4,5]
    outputObject = findNumber(myList)
    if outputObject.findNumbr()!= True:
        print("Number not in list ")
    else:
        print("Number in list ")
