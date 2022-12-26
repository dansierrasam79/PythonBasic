#Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
class findGCD:
    def __init__(self, givenValue1, givenValue2):
        self.value1 = givenValue1
        self.value2 = givenValue2
    def findGreatestCommonDivisor(self):
        return math.gcd(self.value1, self.value2)
#Driver code
if __name__ == "__main__":
    import math
    firstVal = int(input("Enter the first value: "))
    secondVal = int(input("Enter the second value: "))
    outputObject = findGCD(firstVal, secondVal)
    print("GCD: ", outputObject.findGreatestCommonDivisor())
