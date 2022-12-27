# Write a Python program to convert seconds to day, hour, minutes and seconds.
def day(time):
    if time < 86400:
        return 0, time
    else:
        days = round(time/86400)
        timeDays = time - days*86400
        return days, timeDays
def hours(time):
    if time < 3600:
        return 0, time
    else:
        hours = round(time/3600)
        timeSeconds = time - hours*3600
        return hours, timeSeconds
def minutes(time):
    if time < 60:
        return 0, time
    else:
        minutes = round(time/60)
        timeSeconds = time - minutes*60
        return minutes, timeSeconds
#Main
if __name__ == "__main__":
    timeSeconds = int(input("Enter the number of seconds to be converted: "))
    dayRemain, secndsRemain = day(timeSeconds)
    hourRemain, sendsRemain = hours(secndsRemain)
    minutesRemain, secondsRemain = minutes(sendsRemain)
    print("Days:", dayRemain, "Hours:", hourRemain, "Minutes:", minutesRemain, "Seconds:",secondsRemain)
