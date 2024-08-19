# len(list)
my_2d_list = [['apple', 'banana', 'cherry'],
              ['mango', 'kiwi', 'melon'],
              ['orange', 'grape', 'pear']]
rows = len(my_2d_list)
print(rows)  # Output: 3

# list[row_index]
my_2d_list = [['apple', 'banana', 'cherry'],
              ['mango', 'kiwi', 'melon'],
              ['orange', 'grape', 'pear']]
row = my_2d_list[1]
print(row)  # Output: ['mango', 'kiwi', 'melon']

# list[row_index][column_index]
my_2d_list = [['apple', 'banana', 'cherry'],
              ['mango', 'kiwi', 'melon'],
              ['orange', 'grape', 'pear']]
element = my_2d_list[1][2]
print(element)  # Output: 'melon'

# append(row)
my_2d_list = [['apple', 'banana', 'cherry'],
              ['mango', 'kiwi', 'melon']]
new_row = ['orange', 'grape', 'pear']
my_2d_list.append(new_row)
print(my_2d_list)  # Output: [['apple', 'banana', 'cherry'], ['mango', 'kiwi', 'melon'], ['orange', 'grape', 'pear']]

# extend(iterable)
my_2d_list = [['apple', 'banana', 'cherry'],
              ['mango', 'kiwi', 'melon']]
other_list = [['orange', 'grape', 'pear'],
              ['watermelon', 'pineapple', 'lemon']]
my_2d_list.extend(other_list)
print(my_2d_list)  # Output: [['apple', 'banana', 'cherry'], ['mango', 'kiwi', 'melon'], ['orange', 'grape', 'pear'], ['watermelon', 'pineapple', 'lemon']]

# insert(row_index, row)
my_2d_list = [['apple', 'banana', 'cherry'],
              ['mango', 'kiwi', 'melon']]
new_row = ['orange', 'grape', 'pear']
my_2d_list.insert(1, new_row)
print(my_2d_list)  # Output: [['apple', 'banana', 'cherry'], ['orange', 'grape', 'pear'], ['mango', 'kiwi', 'melon']]

# pop(row_index)
my_2d_list = [['apple', 'banana', 'cherry'],
              ['mango', 'kiwi', 'melon'],
              ['orange', 'grape', 'pear']]
popped_row = my_2d_list.pop(1)
print(popped_row)  # Output: ['mango', 'kiwi', 'melon']

# sort()
fruits = ['apple', 'banana', 'cherry', 'mango', 'kiwi', 'melon']
fruits.sort()
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'melon']

# count()
fruits = ['apple', 'banana', 'cherry', 'banana']
count = fruits.count('banana')
print(count)  # Output: 2
