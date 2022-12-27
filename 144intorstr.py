# Write a Python program to check whether a variable is of integer or string.
if __name__ == "__main__":
    aVariable = input("Enter a sequence of characters: ")
    print("Is Integer?:", aVariable.isnumeric())
    print("Is String:?", aVariable.isalpha())
