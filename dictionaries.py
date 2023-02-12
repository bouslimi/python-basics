"""
    Data Structures - Dictionaries (Key / Value pairs)
"""

person = {
    "full_name": "First LAST",
    "age": 30,
    "address": "Tunisia"
}

print(person)
print(person.keys())
print(person.values())

print(person["address"])
print(person.get("address"))

person["address"] = "Egypt"
print(person["address"])
