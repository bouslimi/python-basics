"""
    Formatting Strings
"""

comment = """
        --- Python ---
    Hello World of Python!
        --------------
"""
print(comment)

###

name = "Amine"
age = 30

message = "I'm {} and I have {}."
print(message.format(name, age))

formatted_message = f"I'm {name} and I have {age}."
print(formatted_message)
