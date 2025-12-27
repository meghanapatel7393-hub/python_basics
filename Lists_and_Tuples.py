#A list stores multiple values in one variable.
numbers = [10, 20, 30, 40]
names = ["Amit", "Rahul", "Bhavesh"]

print(names[0])   # Amit
print(names[1])   # Rahul
print(names[-1])  # Bhavesh

#👉 Index starts from 0

#Change List Items
names[1] = "Rohit"
print(names)

#List Functions (Very Important)
nums = [5, 2, 9, 1]
nums.append(7)
nums.insert(1, 100)
nums.remove(2)
nums.pop(0)
nums.sort()

print(nums)

#Loop with List
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

for index in range(len(fruits)):
    print(fruits[index])

#Check Item in List
if "apple" in fruits:
    print("Apple is available")
    
#Tuple - Tuple is like list but cannot be changed
print("Tuple (Read Only List)")
colors = ("red", "green", "blue")
'''
✔ Ordered
❌ Cannot modify
✔ Faster than list
'''
'''
Difference: List vs Tuple
| List       | Tuple          |
| ---------- | -------------- |
| `[]`       | `()`           |
| Changeable | Not changeable |
| Slower     | Faster         |

'''

#Convert List ↔ Tuple
print("Convert List ↔ Tuple")
t = tuple([1, 2, 3])
l = list((4, 5, 6))

print(t,type(t))
print(l,type(l))


'''
When to Use What?

| Data Type  | Use                 |
| ---------- | ------------------- |
| List       | Ordered, changeable |
| Tuple      | Fixed data          |
| Dictionary | Key-value data      |
| Set        | Unique data         |

'''