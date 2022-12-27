#Write a Python program to get an absolute file path.
if __name__ == "__main__":
    import os
    if os.path.abspath("danny.txt") is True:
        print(os.path.abspath("danny.txt"))
    else:
        print("Absolute path not available")
