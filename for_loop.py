"""
    For Loop
"""

# List
students = ["Amine", "Ala", "Karim"]

for student in students:
    print(student)

# Dictionary
person = {
    "full_name": "First LAST",
    "age": 30,
    "countryCode": "TN"
}

for key in person:
    print(f"key: {key} \t value: {person[key]}")

for key, value in person.items():
    print(f"key: {key} \t value: {value}")
