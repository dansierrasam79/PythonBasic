'''Write a Python program to print the following string in a specific format (see the output).

Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"

Output :
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
Twinkle, twinkle, little star,
How I wonder what you are!'''

class mozartPoem:
    def __init__(self, poem):
        self.mPoem = poem

    def displayPoem(self):
        return self.mPoem

#Driver code
if __name__ == "__main__":
    poem = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky.Twinkle, twinkle, little star,How I wonder what you are!"
    outputObject = mozartPoem(poem)
    print(outputObject.displayPoem())


