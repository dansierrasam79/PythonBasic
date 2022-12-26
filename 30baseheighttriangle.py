#Write a Python program that will accept the base and height of a triangle and compute the area.
class computeTriangleArea:
    def __init__(self, givenBase, givenHeight):
        self.base = givenBase
        self.height = givenHeight
    def computeArea (self):
        return (1/2)*self.base*self.height
#Driver code
if __name__ == "__main__":
    acceptedHeight = float(input("Enter triangle height: "))
    acceptedBase = float(input ("Enter triangle base: "))
    outputObject = computeTriangleArea(acceptedHeight, acceptedBase)
    print("Area: ", outputObject.computeArea())
