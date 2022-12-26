#Write a Python program to display your details like name, age, address in three different lines.
class displayDetails:
    def __init__(self, nameValue, ageValue, addressValue):
        self.name = nameValue
        self.age = ageValue
        self.address = addressValue
    def displayDetails(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Address: ", self.address)
# Driver code
if __name__ == "__main__":
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    address = input("Enter address: ")
    outputObject = displayDetails(name, age, address)
    outputObject.displayDetails()
