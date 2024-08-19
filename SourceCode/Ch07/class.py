class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I'm {self.age}")

# Creating an instance of the Person class
user = Person("Alice", 25)



# Accessing attributes and calling methods of the person object
print(user.name)  
print(user.age)  
user.say_hello()  
