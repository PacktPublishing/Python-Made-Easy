class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def display_info(self):
        super().display_info()
        print(f"Grade: {self.grade}")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")


# Creating instances of the classes
student = Student("Alice", 16, 10)
teacher = Teacher("Mr. Smith", 35, "Math")

# Calling the display_info method
student.display_info()
print()
teacher.display_info()
