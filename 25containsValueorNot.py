'''Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False'''

class containsValue:
    def __init__(self, givenList, givenValue):
        self.myList = givenList
        self.myNumber = givenValue
    def checkForValue (self):
        for number in self.myList:
            if number == self.myNumber:
                return True
        return False
#Driver code
if __name__ == "__main__":
    givenList = [1,5,8,3]
    acceptedValue = int(input("Enter search value: "))
    outputValue = containsValue(givenList, acceptedValue)
    print("Value Present: ", outputValue.checkForValue())
