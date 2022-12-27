# Write a program to get execution time for a Python method.
def addition (a,b):
    return a + b
if __name__ == "__main__":
    from datetime import datetime
    start = datetime.now()
    addition(2,3)
    final = datetime.now() - start
    print(final)
