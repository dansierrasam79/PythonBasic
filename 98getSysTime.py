'''Write a Python program to get the system time.
Note : The system time is important for debugging, network information, random number seeds,
or something as simple as program performance.'''
if __name__ == "__main__":
    import datetime
    print(datetime.datetime.now().time())
