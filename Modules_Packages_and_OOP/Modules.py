#A module is a Python file with reusable code.

#Built-in Module Example
import math

print(math.sqrt(25))
print(math.pi)


# Import Specific Function
from math import sqrt, pi

print(sqrt(25))
print(pi)

#Create Your Own Module
import mymodule

print(mymodule.add(10, 20))


#Packages
# Package = folder of modules
'''
structure
mypackage/
  ├── __init__.py
  ├── file1.py
  └── file2.py

  import

  from mypackage import file1

'''