# Write a Python program to extract single key-value pair of a dictionary in variables.
if __name__ == "__main__":
    myDict = {1:"Daniel", 2:"Nutan", 3:"Swapan", 4: "Mark", 5:"Mohan"}
    aVariable = int(input("Enter a key or value: "))
    for key, value in myDict.items():
        if int(aVariable) == key or aVariable == value:
            myKey = key
            myValue = value
            break;
    print("After extraction: ", myKey, myValue)
