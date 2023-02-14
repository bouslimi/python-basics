"""
    Functions
"""


def greet(name, country):
    print(f"Hello {name} from {country}!")


greet("Amine", "Tunisia")

# Return values from functions


def is_adult(age):
    return age >= 16


print(is_adult(14))
print(is_adult(32))
