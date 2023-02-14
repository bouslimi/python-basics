"""
    Classes
    (Use CamelCase for class's name)
"""


class SmartPhone:

    # Constructor
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self, phone_number):
        print(f"{self.brand} is calling {phone_number}...")

    # Override __str__ (toString method)
    def __str__(self) -> str:
        return f"Smartphone brand is {self.brand} and its price is {self.price} CAD."


# Create an object from class
myphone = SmartPhone("Galaxy S21", 900)

print(myphone.brand)
myphone.call(911)

print(myphone)
