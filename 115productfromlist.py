# Write a Python program to compute the product of a list of integers (without using for loop).
count = 0
total = 1
myList = [1,2,3, 4, 5, 6, 7, 8, 9, 10]
def product(c,t):
    if c == len(myList):
        return t
    else:
        t=t*myList[c]
        c = c+1
    return product(c,t)
if __name__ == "__main__":
    output = product(count, total)
    print("The product of the list of numbers is: ", output)
