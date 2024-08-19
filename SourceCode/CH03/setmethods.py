# Creating a set
my_set = {'apple', 'banana', 'cherry'}
print(my_set)  # Output: {'apple', 'banana', 'cherry'}

# add(element)
my_set.add('orange')
print(my_set)  # Output: {'apple', 'banana', 'cherry', 'orange'}

# remove(element)
my_set.remove('banana')
print(my_set)  # Output: {'apple', 'cherry', 'orange'}

# discard(element)
my_set.discard('cherry')
print(my_set)  # Output: {'apple', 'orange'}

# pop()
popped_element = my_set.pop()
print(popped_element)  # Output: 'apple'
print(my_set)  # Output: {'orange'}

# clear()
my_set.clear()
print(my_set)  # Output: set()

# union(other_set)
set1 = {'apple', 'banana', 'cherry'}
set2 = {'cherry', 'orange', 'kiwi'}
union_set = set1.union(set2)
print(union_set)  # Output: {'apple', 'banana', 'cherry', 'orange', 'kiwi'}

# intersection(other_set)
set1 = {'apple', 'banana', 'cherry'}
set2 = {'cherry', 'orange', 'kiwi'}
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {'cherry'}

# difference(other_set)
set1 = {'apple', 'banana', 'cherry', 'orange'}
set2 = {'cherry', 'orange', 'kiwi'}
difference_set = set1.difference(set2)
print(difference_set)  # Output: {'apple', 'banana'}

# symmetric_difference(other_set)
set1 = {'apple', 'banana', 'cherry'}
set2 = {'cherry', 'orange', 'kiwi'}
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {'apple', 'banana', 'orange', 'kiwi'}
