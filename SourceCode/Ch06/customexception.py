class InvalidInputError(Exception):
    def __init__(self, message):
        self.message = message

def calculate_factorial(n):
    if not isinstance(n, int) or n < 0:
        raise InvalidInputError("Invalid input. Please provide a non-negative integer.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

try:
    num = int(input("Enter a non-negative integer: "))
    result = calculate_factorial(num)
    print("Factorial:", result)
except InvalidInputError as e:
    print("Error:", e.message)
