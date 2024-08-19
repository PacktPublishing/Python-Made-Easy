def calculate_average(numbers):
    if not numbers:
        return None  
    total = sum(numbers)  
    average = total / len(numbers)  
    return average

def find_maximum(numbers):
    if not numbers:
        return None 
    maximum = numbers[0]  
    for num in numbers:
        if num > maximum:
            maximum = num  
    return maximum
