# Write a Python program to check whether a file path is a file or a directory.
if __name__ == "__main__":
    import os
    filePath = "/home/danielchakraborty/Desktop/composition.txt"
    dirPath = "/home/danielchakraborty/Desktop"
    print("Is file?:", os.path.isfile(filePath))
    print("Is directory?", os.path.isdir(dirPath))
