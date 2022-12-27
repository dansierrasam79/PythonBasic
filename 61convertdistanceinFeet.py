# Write a Python program to convert the distance (in feet) to inches, yards, and miles.
if __name__ == "__main__":
    feet = float(input("Please enter the distance in feet: "))
    #Feet to Inches
    print("The conversion from feet to inches is: ", feet*12)
    #Feet to yards
    print("The conversion from feet to yards is: ", feet*(1/3))
    #Feet to miles
    print("The conversion from feet to miles is: ", feet*0.000189394)
