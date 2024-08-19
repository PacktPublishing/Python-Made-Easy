def greeting_decorator(func):
    def wrapper():
        print("Hello!")
        func()
        print("Goodbye!")
    return wrapper

@greeting_decorator
def greeting():
    print("Welcome!")
    
greeting()
