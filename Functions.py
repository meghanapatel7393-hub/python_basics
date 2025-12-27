print("A function is a reusable block of code.")

def my_function():
  print("Hello from a function")

#Call the function:
my_function()

#Function with Return Value
def add(a, b):
    return a + b

result = add(10, 20)
print(result)


#Function with Input
def square(num):
    return num * num

n = int(input("Enter number: "))
print(square(n))

#Default Parameters
def country(name="India"):
    print("Country:", name)

country()
country("USA")

#Multiple Return Values
def calc(a, b):
    return a+b, a-b, a*b

add, sub, mul = calc(10, 5)
print(add, sub, mul)

#Arbitrary Arguments
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#Keyword Arguments
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#Arbitrary Keyword Arguments
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


#Local vs Global Variable
x = 10  # global

def test():
    x = 5  # local
    print(x)

test()
print(x)

'''
Why Functions Matter?

✔ Clean code
✔ Reusability
✔ Easy debugging
✔ Interview favorite
'''