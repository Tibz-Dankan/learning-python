# Python Classes/Objects

# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# Declare a class
class MyClass:
  x = 5

# Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)


# The __init__() Function
# Use the __init__() function to assign values to object properties, 
# or other operations that are necessary to do when the object is being created:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


# The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)


# Modify Object Properties
# Set the age of p1 to 40:
p1.age = 40

# Delete Object Properties
del p1.age


