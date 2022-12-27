# Write a Python program to calculate the sum over a container.
if __name__ == "__main__":
    myTuple = (1,2,3,4,5,6)
    total = 0
    for item in myTuple:
        total = total + item
    print(total)
