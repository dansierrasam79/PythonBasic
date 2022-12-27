#Write a Python program to print to stderr.
if __name__ == "__main__":
    import sys
    print("Hello World!")
    sys.stderr.write("Hello World!")
