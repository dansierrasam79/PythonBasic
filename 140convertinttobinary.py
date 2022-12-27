'''Write a Python program to convert an integer to binary keep leading zeros.
Sample data : x=12
Expected output : 00001100
0000001100'''
if __name__ == "__main__":
    aVariable = int(input("Enter a decimal number: "))
    print("Binary equivalent: ", bin(aVariable))
