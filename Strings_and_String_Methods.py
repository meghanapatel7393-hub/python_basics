#A string is text inside quotes.
text = "Python"

print(text[0])   # P
print(text[3])   # h
print(text[-1])  # n
print(len(text))

#String Slicing
text = "Python Programming"

print(text[0:6])   # Python
print(text[7:18])  # Programming
print(text[:6])    # Python
print(text[7:])    # Programming


#String Methods

'''
| Method    | Use           |
| --------- | ------------- |
| upper()   | CAPITAL       |
| lower()   | small         |
| strip()   | remove spaces |
| replace() | replace text  |
| find()    | find index    |
| count()   | count word    |
| split()   | split words   |

'''

msg = " hello Python "

print(msg.upper())
print(msg.strip())
print(msg.replace("Python", "World"))
print(msg.split())

#String Concatenation
first = "Hello"
second = "World"

print(first + " " + second)

#f-string
name = "Bhavesh"
age = 22

print(f"My name is {name} and age is {age}")

#Check Substring
text = "Python is easy"

if "Python" in text:
    print("Yes, found")

#Loop Through String
for ch in "Python":
    print(ch)

#String Format
name = "Bhavesh"
age = 22

print("My name is {} and age is {}".format(name, age))
print("My name is {} and age is {}".format("Bhavesh", 22))
print("My name is {0} and age is {1}".format("Bhavesh", 22))
print("My name is {name} and age is {age}".format(name="Bhavesh", age=22))

#String Template
name = "Bhavesh"
age = 22

print(f"My name is {name} and age is {age}")

#reverse String
name = "Bhavesh"
print(name[::-1])
