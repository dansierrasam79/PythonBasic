#Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.
def conversion():
    print("*******Menu Options********")
    print("1. Kilopascals to pounds per square inch")
    print("2. Kilopascals to mmHg")
    print("3. Kilopascals to atmosphere pressure")
    print("4. Exit")
    userInput = input("Select a menu option")
    if userInput == "1":
        kp = float(input("Please enter the pressure in kilopascals: "))
        psi = kp*0.145038
        print("The pressure in pounds per square inch is:", psi)
    elif userInput == "2":
        kp = float(input("Please enter the pressure in kilopascals: "))
        mmhg = kp*7.50062
        print("The pressure in millimeter of mercury is:", mmhg)
    elif userInput == "3":
        kp = float(input("Please enter the pressure in kilopascals: "))
        ap = kp*0.00986923
        print("The pressure in atmospheres is:", ap)
    else:
        print("Bye bye!")
#Main
if __name__ == "__main__":
    conversion()
    while True:
        usrInpt = input("Do you wish to continue (y/n)?")
        if usrInpt == "y" or usrInpt == "Y":
            conversion()
        else:
            print("Thank you for using this menu for your calculations! Bye Bye")
            break;
