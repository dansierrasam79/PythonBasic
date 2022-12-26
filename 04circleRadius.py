'''Write a Python program which accepts the radius of a circle from the user and compute the
area.
Sample Output :
r = 1.1
Area = 3.8013271108436504'''

class areaCircle:
    def __init__(self, givenRadius, givenPi):
        self.radius = givenRadius
        self.piValue = givenPi
    def computeArea (self):
        return self.piValue*self.radius*self.radius

#Driver code
if __name__ == "__main__":
    import math
    gRadius = float (input("Enter a radius value: "))
    outputObject = areaCircle(gRadius, math.pi)
    print(outputObject.computeArea())
