"""
    Data Structures - Lists
"""

numbers_list = [5, 0, -1, 5, 2]

numbers_list.append(-7)
print(numbers_list)

print(-1 in numbers_list)

print(len(numbers_list))

numbers_list.sort()
print(numbers_list)

# removes only the first occurence. To remove all occurences # while(5 in numbers_list): numbers_list.remove(5)
numbers_list.remove(5)
print(numbers_list)

del numbers_list[0]
print(numbers_list)

numbers_list.clear()
print(numbers_list)
