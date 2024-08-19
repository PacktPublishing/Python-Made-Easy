# String methods
text = "Python programming language is versatile and powerful."

# length of the string using len() method
length = len(text)
print(length)  # Output: 49

# converting the string to uppercase using upper() method
uppercase_text = text.upper()
print(uppercase_text)  # Output: PYTHON PROGRAMMING LANGUAGE IS VERSATILE AND POWERFUL.

# converting the string to lowercase using lower() method
lowercase_text = text.lower()
print(lowercase_text)  # Output: python programming language is versatile and powerful.

# checking if the string starts with a specific substring using startswith() method
starts_with_python = text.startswith("Python")
print(starts_with_python)  # Output: True

# checking if the string ends with a specific substring using endswith() method
ends_with_powerful = text.endswith("powerful.")
print(ends_with_powerful)  # Output: True

# finding the index of a substring using find() method
index_of_language = text.find("language")
print(index_of_language)  # Output: 19

# replacing a substring with another string using replace() method
replaced_text = text.replace("versatile", "flexible")
print(replaced_text)  # Output: Python programming language is flexible and powerful.

# splitting the string into a list of substrings using split() method
split_text = text.split(" ")
print(split_text)  # Output: ['Python', 'programming', 'language', 'is', 'versatile', 'and', 'powerful.']

# joining a list of substrings into a single string using join() method
joined_text = "-".join(split_text)
print(joined_text)  # Output: Python-programming-language-is-versatile-and-powerful.

# stripping leading and trailing whitespace using strip() method
whitespace_text = "   Python programming language is versatile and powerful.   "
stripped_text = whitespace_text.strip()
print(stripped_text)  # Output: Python programming language is versatile and powerful.
