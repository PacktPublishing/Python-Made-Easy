def greet(name):
    if len(name) > 0:
        print("Hello, " + name + "!")
    else:
        print("Hello there!")
    print("Nice to meet you.")

greet("Alice")
greet("Bob")
greet("")