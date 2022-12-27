# Write a Python program to determine whether a variable is defined or not.
if __name__ == "__main__":
    variable = input("Enter anything: ")
    try:
        print("Declared variable: ", variable)
    except NameError:
        print("Variable isn't declared")
