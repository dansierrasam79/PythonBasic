#Write a Python program to get the volume of a sphere with radius 6.

class volumeSphere:
    def __init__(self, givenRadius):
        self.radius = givenRadius
    def computeVolume (self):
        return math.pi*math.pow(self.radius,3)
    
#Driver code
if __name__ == "__main__":
    import math
    #Enter 6 as radius value
    givenRad = float (input ("Enter the radius: "))
    outputObject = volumeSphere (givenRad)
    print("Volume: ", outputObject.computeVolume())
