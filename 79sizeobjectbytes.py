# Write a Python program to get the size of an object in bytes.
if __name__ == "__main__":
    import sys
    x = 2
    y = 5.0
    z = "Daniel"
    print(sys.getsizeof(x))
    print(sys.getsizeof(y))
    print(sys.getsizeof(z))
