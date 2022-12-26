#Write a Python program to test whether a passed letter is a vowel or not.
class vowelOrNot:
    def __init__(self, givenLetter):
        self.letter = givenLetter
    def vowelCheck (self):
        vowelsList = ["a", "e", "i", "o", "u"]
        for letter in vowelsList:
            if self.letter == letter:
                return True
        return False
#Driver code
if __name__ == "__main__":
    letter = input("Enter an alphabet: ")
    outputObject = vowelOrNot (letter)
    if outputObject.vowelCheck() == True:
        print("Is a vowel")
    else:
        print("Is NOT a vowel")
