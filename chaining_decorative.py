#Chaining Decorators
def deco1(func):
  def wrapper():
    print("Deco1")
    func()
    return
  return wrapper

def deco2(func):
  def wrapper():
    print("Deco2")
    func()
    return
  return wrapper

@deco1
@deco2
def hello():
  print("Hello")

hello()


#Decorators with Arguments
def decorator(func):
  def wrapper(name):
    print("Before function")
    func(name)
    print("After function")
  return wrapper

@decorator
def greet(name):
  print(f"Hello {name}")

greet("Bhavesh")

#Simple Decorator Example
def decorator(func):
  def wrapper():
    print("Before function")
    func()
    print("After function")
  return wrapper

@decorator
def say_hello():
  print("Hello World")

say_hello()