#Write a Python program to input a number, if it is not a number generate an error message.
def usrInput():
    try:
        userInput = int(input("Enter a integer using numbers from 0-9: "))
        print("Your input was right.", userInput, " was an integer.")
    except ValueError:
        print("Your input was incorrect. Please try again: ")
        usrInput()
if __name__ == "__main__":
    usrInput()
    print("Good for you! You follow instructions well! No more repetition.")
