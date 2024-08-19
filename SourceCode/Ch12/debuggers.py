def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

numbers = [1, 2, 3, 4, 5]
result = calculate_average(numbers)
print("The average is:", result)

