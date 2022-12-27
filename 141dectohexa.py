'''Write a python program to convert decimal to hexadecimal.
Sample decimal number: 30, 4
Expected output: 1e, 04'''
if __name__ == "__main__":
    givenValue = int(input("Enter a decimal number: "))
    print("The hexadecimal equivalent of ", givenValue, " is ", hex(givenValue))
