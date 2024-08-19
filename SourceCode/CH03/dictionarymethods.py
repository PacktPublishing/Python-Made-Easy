# Creating a dictionary
student_scores = {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'Diana': 92}
print(student_scores)  # Output: {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'Diana': 92}

# Accessing values using keys
alice_score = student_scores['Alice']
print(alice_score)  # Output: 85

# Using get() method to access values with default value
bob_score = student_scores.get('Bob', 0)
eve_score = student_scores.get('Eve', 0)
print(bob_score)  # Output: 90
print(eve_score)  # Output: 0

# Checking if a key exists in the dictionary
is_charlie_present = 'Charlie' in student_scores
is_eve_present = 'Eve' in student_scores
print(is_charlie_present)  # Output: True
print(is_eve_present)  # Output: False

# Modifying values
student_scores['Charlie'] = 80
student_scores['Eve'] = 88
print(student_scores)  # Output: {'Alice': 85, 'Bob': 90, 'Charlie': 80, 'Diana': 92, 'Eve': 88}

# Removing a key-value pair
del student_scores['Bob']
print(student_scores)  # Output: {'Alice': 85, 'Charlie': 80, 'Diana': 92, 'Eve': 88}

# Getting all keys, values, and items
keys = student_scores.keys()
values = student_scores.values()
items = student_scores.items()
print(keys)  # Output: dict_keys(['Alice', 'Charlie', 'Diana', 'Eve'])
print(values)  # Output: dict_values([85, 80, 92, 88])
print(items)  # Output: dict_items([('Alice', 85), ('Charlie', 80), ('Diana', 92), ('Eve', 88)])

# Updating the dictionary with another dictionary
additional_scores = {'Frank': 95, 'Grace': 88}
student_scores.update(additional_scores)
print(student_scores)  # Output: {'Alice': 85, 'Charlie': 80, 'Diana': 92, 'Eve': 88, 'Frank': 95, 'Grace': 88}

# Removing and returning an arbitrary key-value pair
removed_item = student_scores.popitem()
print(removed_item)  # Output: ('Grace', 88)
print(student_scores)  # Output: {'Alice': 85, 'Charlie': 80, 'Diana': 92, 'Eve': 88, 'Frank': 95}

# Clearing the dictionary
student_scores.clear()
print(student_scores)  # Output: {}
