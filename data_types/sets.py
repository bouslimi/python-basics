"""
    Data Structures - Sets
"""

numbers_set = {5, 0, -1, 5, 2}   # Duplicates will be removed (like 5 here)
print(numbers_set)   # Sets are not ordered

other_set = {8, 10, 2, 0}
print(other_set)

# Union
union_set = numbers_set | other_set  # Duplicates will be removed (like 1 here)
print(f"Union = {union_set}")

# Intersection
intersection_set = numbers_set & other_set
print(f"Intersection = {intersection_set}")

empty_intersection_set = numbers_set & {999, 888}  # Returns # set()
print(f"emptyintersection_set = {empty_intersection_set}")

# Difference
difference_set = numbers_set - other_set
print(f"Difference = {difference_set}")
