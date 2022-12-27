# Write a Python program to calculate body mass index.
if __name__ == "__main__":
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    bmi = weight/height
    print("Your body mass index is: ", bmi)
