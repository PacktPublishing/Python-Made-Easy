def factorial(n):
    if n <= 1:
        return 1
    else:
        a = n * factorial(n-1)
        return a

print (factorial(4))
