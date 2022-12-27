# Write a Python program to get file creation and modification date/times.
if __name__ == "__main__":
    import os, time
    mawDate = os.path.getmtime(r"C:\Users\Programming\Desktop\composition.txt")
    creation = os.path.getctime(r"C:\Users\Programming\Desktop\composition.txt")
    print("The creation time of said file is: ", time.ctime(creation))
    print("The last modification time of said file is: ", time.ctime(mawDate))
