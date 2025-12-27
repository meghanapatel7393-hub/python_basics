#What are Dunder Methods?
#Dunder methods (double underscore methods) are special methods in Python that start and end with __.

#“Dunder methods allow us to define the behavior of objects for built-in operations.”

'''
2. Common Dunder Methods

Method	    |   Purpose
__init__	  |   Constructor
__str__	    |   Readable string representation
__repr__	  |   Official representation
__len__	    |   Length of object
__add__	    |   Addition operator
'''


#3. __str__ vs __repr__
class User:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f"Users: {self.name}"

  def __repr__(self):
    return f"User('{self.name}')"
  
  
u1 = User("Bhavesh")
print(u1)
print(u1.__str__())
print(u1.__repr__())

print(str(u1))
print(repr(u1))

'''
__str__ → for users
__repr__ → for developers

'''

#__len__ Example
class Cart:
  def __init__(self, items):
    self.items = items

  def __len__(self):
    return len(self.items)
cart = Cart([1, 2, 3])
print(len(cart))


#Operator Overloading
#Operator overloading allows operators to behave differently for custom objects.
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y)
p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2
print(p3.x, p3.y)
#+ uses __add__ internally.

