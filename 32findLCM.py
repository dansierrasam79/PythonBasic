#Write a Python program to get the least common multiple (LCM) of two positive integers.
class findLCM:
    def __init__(self, givenValue1, givenValue2):
        self.value1 = givenValue1
        self.value2 = givenValue2
    def findLeastCommonMultiple(self):
        return math.lcm(self.value1, self.value2)
#Driver code
if __name__ == "__main__":
    import math
    firstVal = int(input("Enter the first value: "))
    secondVal = int(input("Enter the second value: "))
    outputObject = findLCM(firstVal, secondVal)
    print("LCM: ", outputObject.findLeastCommonMultiple())
