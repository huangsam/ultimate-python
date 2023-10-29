"""
Understanding the __init__ Method in Python Classes
"""

# Basic __init__ Method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Person classes
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print("Basic __Init__ Method's output:")
print(f"{person1.name} is {person1.age} years old.")
print(f"{person2.name} is {person2.age} years old.")

# Default Values in __init__
class Book:
    def __init__(self, title, author="Unknown"):
        self.title = title
        self.author = author

# Book class with and without specifying the author
book1 = Book("Python Programming")
book2 = Book("Machine Learning", "John Smith")

print("\nBook class with and without specifying the author : ")
print(f"Book 1: {book1.title} by {book1.author}")
print(f"Book 2: {book2.title} by {book2.author}")

# Complex __init__ Method
class Car:
    def __init__(self, make, model, year, color="Black"):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = 0

    def drive(self, miles):
        self.mileage += miles

# Car class and using the drive method
car1 = Car("Toyota", "Camry", 2022, "Blue")
car1.drive(100)

print("\nCar class and using the drive method:")
print(f"Car Make: {car1.make}")
print(f"Car Model: {car1.model}")
print(f"Car Year: {car1.year}")
print(f"Car Color: {car1.color}")
print(f"Car Mileage: {car1.mileage} miles")

# Inheritance and __init__
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class CollegeStudent(Student):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

college_student = CollegeStudent("Emma", 20, "Computer Science")

print("\nInheritance:")
print(f"College Student: {college_student.name}, {college_student.age}, {college_student.major}")
