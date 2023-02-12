"""
    Control Flow (if statement)
"""

number = -4

if (number > 0):
    print(f"The number {number} is posotive.")
elif (number < 0):
    print(f"The number {number} is negative.")
else:
    print(f"The number {number} is zero.")

"""
    Control Flow (ternary operators)
"""

country_code = "TN"
message = "Tunisian nationality" if (
    country_code == "TN") else "Other nationality"
print(message)
