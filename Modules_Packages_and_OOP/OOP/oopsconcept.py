#Class & Object
class Student:
    name = "Bhavesh"
    age = 22

s1 = Student()
print(s1.name)
print(s1.age)


#__init__ Constructor
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Bhavesh", 22)
s2 = Student("Amit", 23)

print(s1.name, s1.age)


#Methods in Class
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)

s = Student("Bhavesh")
s.greet()


'''
self Keyword (IMPORTANT)

Refers to current object

Mandatory in class methods
'''

#Inheritance
class Person:
    def speak(self):
        print("I am a person")

class Student(Person):
    def study(self):
        print("I am studying")

s = Student()
s.speak()
s.study()
