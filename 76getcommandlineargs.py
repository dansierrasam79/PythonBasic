# Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.
if __name__ == "__main__":
    import sys
    programName = sys.argv[0]
    argumentNum = sys.argv[1:]
    count = len(sys.argv)
    print(programName, count, str(argumentNum))
