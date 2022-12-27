# Write a Python function to check whether a number is divisible by another number. Accept two integers values form the user.
if __name__ == "__main__":
    aVariable = int(input("Enter the first number: "))
    bVariable = int(input("Enter the second number: "))
    if aVariable%bVariable == 0 or bVariable % aVariable == 0:
        print("The numbers are divisible.")
    else:
        print("The numbers are NOT divisible")
