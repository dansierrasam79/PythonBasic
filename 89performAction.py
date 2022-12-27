'''Write a Python program to perform an action if a condition is true.
Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.'''
if __name__ == "__main__":
    userInput = int(input("Enter any number: "))
    if userInput == 1:
        print("First day of a Month")
