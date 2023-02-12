"""
    Dates
"""

from datetime import datetime

print(datetime.now())
print(datetime.now().date())
print(datetime.now().date().year)
print(datetime.now().time())
print(datetime.now().time().hour)

print("######  Formatting date  #####")

actual_datetime = datetime.now()
print(actual_datetime)
print(actual_datetime.strftime("%d/%m/%Y %H:%M:%S"))
print(actual_datetime.strftime("%d %B %Y %H:%M:%S"))
print(actual_datetime.strftime("%d %b %Y %H:%M:%S"))
