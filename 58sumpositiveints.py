# Write a python program to find the sum of the first n positive integers.
if __name__ == "__main__":
    n = int(input("Enter any positive integer: "))
    total = 0
    for i in range(1,n+1,1):
        total = total + i
    print(total)
