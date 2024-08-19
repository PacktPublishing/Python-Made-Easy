# index(element)
my_tuple = ('apple', 'banana', 'cherry', 'banana')
index = my_tuple.index('banana')
print(index)  # Output: 1

# count(element)
my_tuple = ('apple', 'banana', 'cherry', 'banana')
count = my_tuple.count('banana')
print(count)  # Output: 2

# len(tuple)
my_tuple = ('apple', 'banana', 'cherry')
length = len(my_tuple)
print(length)  # Output: 3

# accessing tuple elements
my_tuple = ('apple', 'banana', 'cherry')
print(my_tuple[0])  # Output: 'apple'

# iterating over a tuple
my_tuple = ('apple', 'banana', 'cherry')
for item in my_tuple:
    print(item)

# converting tuple to list
my_tuple = ('apple', 'banana', 'cherry')
my_list = list(my_tuple)
print(my_list)  # Output: ['apple', 'banana', 'cherry']

# converting list to tuple
my_list = ['apple', 'banana', 'cherry']
my_tuple = tuple(my_list)
print(my_tuple)  # Output: ('apple', 'banana', 'cherry')
