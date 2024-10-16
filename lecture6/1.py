from itertools import groupby
from operator import itemgetter

# List of students with their names and ages
students = [{'name': 'Ana', 'age': 25}, {'name': 'Alexandre', 'age': 21}, {'name': 'Katevan', 'age': 26}, {'name': 'Giorgi', 'age': 26}]

# Sort the list of students by 'age' to prepare for grouping
students.sort(key=itemgetter('age'))

# Group students by 'age' using itertools.groupby, grouping by 'age' value
students = groupby(students, key=itemgetter('age'))

# Iterate through each group and print the age (key) and the corresponding students (group)
for key, group in students:
    print(f"Age {key}: {list(group)}")


from itertools import dropwhile

# List of numbers
numbers = [2, 3, 4, 2, 3, 4, 5, 6, 7, 8, 9]

# dropwhile will drop elements from the list as long as the condition x % 2 == 0 (even number) is True
numbers = list(dropwhile(lambda x: x % 2 == 0, numbers))

# Print the resulting list after dropwhile
print(numbers)