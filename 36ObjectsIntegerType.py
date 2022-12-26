#Write a Python program to add two objects if both objects are an integer type.
class integerTypeTwo:
    def __init__(self, gvalue1, gvalue2):
        self.value1 = gvalue1
        self.value2 = gvalue2
    def addTwoObjects(self):
        if type(self.value1) == int and type (self.value2) == int:
            return self.value1 + self.value2
        else:
            return "No value"
# Driver code
if __name__ == "__main__":
    givenValue1 = int(input("Enter a value: "))
    givenValue2 = int(input("Enter a value: "))
    outputObject = integerTypeTwo(givenValue1, givenValue2)
    print(outputObject.addTwoObjects())
