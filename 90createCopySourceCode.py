# Write a Python program to create a copy of its own source code.
def file_copy(src, dest):
    with open(src) as f, open(dest, 'w') as d:
        d.write(f.read())
if __name__ == "__main__":
    print("Copying source code...")
    file_copy("test.py","test2.py")
    print("Done...")
    with open("test2.py", "r") as fileReader:
        for line in fileReader:
            print(line, end = '')
