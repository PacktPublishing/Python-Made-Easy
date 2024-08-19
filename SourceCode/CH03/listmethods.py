# append(element)
my_list = ['apple', 'banana', 'cherry']
my_list.append('orange')  # Append 'orange' to the end of the list
print(my_list)  # Output: ['apple', 'banana', 'cherry', 'orange']

# extend(iterable)
my_list = ['apple', 'banana', 'cherry']
my_list.extend(['mango', 'kiwi'])  # Extend the list with elements from the iterable
print(my_list)  # Output: ['apple', 'banana', 'cherry', 'mango', 'kiwi']

# insert(index, element)
my_list = ['apple', 'banana', 'cherry']
my_list.insert(1, 'grape')  # Insert 'grape' at index 1
print(my_list)  # Output: ['apple', 'grape', 'banana', 'cherry']

# remove(element)
my_list = ['apple', 'banana', 'cherry', 'banana']
my_list.remove('banana')  # Remove the first occurrence of 'banana'
print(my_list)  # Output: ['apple', 'cherry', 'banana']

# pop(index)
my_list = ['apple', 'banana', 'cherry']
popped_element = my_list.pop(1)  # Remove and return the element at index 1
print(popped_element)  # Output: 'banana'
print(my_list)  # Output: ['apple', 'cherry']

# index(element)
my_list = ['apple', 'banana', 'cherry', 'banana']
index = my_list.index('banana')  # Find the index of the first occurrence of 'banana'
print(index)  # Output: 1

# count(element)
my_list = ['apple', 'banana', 'cherry', 'banana']
count = my_list.count('banana')  # Count the number of occurrences of 'banana'
print(count)  # Output: 2

# sort()
my_list = ['grape', 'apple', 'cherry', 'banana']
my_list.sort()  # Sort the list in ascending order
print(my_list)  # Output: ['apple', 'banana', 'cherry', 'grape']

# reverse()
my_list = ['apple', 'banana', 'cherry']
my_list.reverse()  # Reverse the order of the elements in the list
print(my_list)  # Output: ['cherry', 'banana', 'apple']

# copy()
my_list = ['apple', 'banana', 'cherry']
new_list = my_list.copy()  # Create a shallow copy of the list
print(new_list)  # Output: ['apple', 'banana', 'cherry']
