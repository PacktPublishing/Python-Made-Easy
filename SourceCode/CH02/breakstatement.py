# Sum of numbers using break statement
sum = 0

while True:
    number = int(input("Enter a number (enter 0 to stop): "))

    if number == 0:
        break   # causes the program to jump out of the loop and continue with the next line of code after the loop

    sum += number

print("The sum of the numbers is:", sum)



