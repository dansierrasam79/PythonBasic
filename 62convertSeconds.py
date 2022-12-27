# Write a Python program to convert all units of time into seconds.
if __name__ == "__main__":
    print("We will convert all units of time to seconds")
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))
    conHours = hours * 60 * 60
    conMinutes = minutes * 60
    totalSeconds = conHours + conMinutes + seconds
    print("The total number of entered time in seconds: ", totalSeconds)
