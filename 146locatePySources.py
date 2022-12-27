# Write a Python program to find the location of Python module sources.
if __name__ == "__main__":
    import imp
    print("Finding the directory of the os module")
    print(imp.find_module('sys'))
