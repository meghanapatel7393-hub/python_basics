#Dictionary (Key–Value Pair)
'''
Dictionary stores data as key : value

👉 Real-life example:

Name → Bhavesh

Age → 22

'''

student = {
    "name": "Bhavesh",
    "age": 22,
    "marks": 85
}

#Access Dictionary Values
#⚠️ Keys must exist, otherwise error.
print(student["name"])
print(student["age"])
print(student["marks"])
print("⚠️ Keys must exist, otherwise error.")

#Safe way:
print(student.get("marks"))
# key does not exist then return None
print(student.get("roll"))

#Change & Add Data
student["age"] = 23
student["city"] = "Mumbai"

print(student)

#Delete Data
del student["city"]
print(student)

#Loop through Dictionary
for key in student:
    print(key, student[key])

for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, value)

#Check if Key Exists
print("name" in student)
print("roll" in student)

#Check if Value Exists
print("Bhavesh" in student.values())
print("Bhavesh" in student)

#Dictionary Comprehension
numbers = {i: i * 2 for i in range(1, 6)}
#output {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
print(numbers)



#Set (Unique Values Only)

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
#Set Functions
print(set1 | set2)  # Union
print(set1 & set2)  # Intersection
print(set1 - set2)  # Difference
print(set1 ^ set2)  # Symmetric Difference

a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))


#Check if Element Exists
print(3 in set1)
print(8 in set1)

#Add Element
set1.add(6)
print(set1)

#Remove Element 
set1.remove(6)
print(set1)

#Clear Set
set1.clear()
print(set1)

#Loop through Set
for i in set1:
    print(i)

for i in set2:
    print(i, end=" ")

print("")

#Set Comprehension
numbers = {i for i in range(1, 6)}
#output {1, 2, 3, 4, 5}
print(numbers)

'''
When to Use What?

| Data Type  | Use                 |
| ---------- | ------------------- |
| List       | Ordered, changeable |
| Tuple      | Fixed data          |
| Dictionary | Key-value data      |
| Set        | Unique data         |

'''