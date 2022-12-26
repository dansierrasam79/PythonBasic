#Write a Python program to find out the number of CPUs using.
if __name__ == "__main__":
    import psutil
    print(psutil.cpu_count())
