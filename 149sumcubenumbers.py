# Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number.
def retCubeValue(number):
    cubeList = []
    for i in range(1, number+1):
        cubeValue = i**3
        cubeList.append(cubeValue)
    return cubeList
if __name__ == "__main__":
    aVariable = int(input("Enter a number: "))
    print(retCubeValue(aVariable))
