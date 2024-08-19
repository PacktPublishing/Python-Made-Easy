# Odd and Even number separation with break and continue statements
start = 1
end = 10

print("Odd numbers:")
# Loop to print odd numbers
for number in range(start, end + 1):
    # Check if number is even
    if number % 2 == 0:
        # Skip even numbers. The continue statement causes the program to jump back to the beginning of the loop and evaluate the loop condition again
        continue

    # Print the odd number
    print(number)

print("\nEven numbers:")
# Loop to print even numbers
for number in range(start, end + 1):
    # Check if number is odd
    if number % 2 != 0:
        # Skip odd numbers
        continue

    # Print the even number
    print(number)
