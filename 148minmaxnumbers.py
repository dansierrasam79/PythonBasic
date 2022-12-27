'''Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
Note: Do not use built-in functions.'''
def getMax(myList):
    maxValue = myList[0]
    for item in myList:
        if item > maxValue:
            maxValue = item
    return maxValue
def getMin(myList):
    minValue = myList[0]
    for item in myList:
        if item < minValue:
            minValue = item
    return minValue
if __name__ == "__main__":
    aList = [4,2,1,5,6,7,9]
    print(getMax(aList))
    print(getMin(aList))
