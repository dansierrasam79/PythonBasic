# Write a Python program to swap two variables.
if __name__ == "__main__":
    aVar = 1
    bVar = 0
    print(aVar, bVar)
    tempVar = aVar
    aVar = bVar
    bVar =tempVar
    print(aVar, bVar)
