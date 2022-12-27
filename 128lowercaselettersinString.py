# Write a Python program to check whether lowercase letters exist in a string.
if __name__ == "__main__":
    aVariable = input("Enter a string: ")
    for char in aVariable:
        if char.islower():
            print("Lower case letter ", char, " exists")
