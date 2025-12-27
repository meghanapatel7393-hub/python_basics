#unittest is Python’s built-in testing framework, inspired by Java’s JUnit.

'''
Test file name

Must start with: test_

🔹 Test function name 
Must start with: test_

Assertions (core of pytest)
assert 5 == 5        # pass
assert 5 > 2         # pass
assert "a" in "cat"  # pass
assert 5 == 3        # fail ❌
pytest automatically shows clear error messages when a test fails.

'''


import unittest

def add(a, b):
  return a + b

class TestMath(unittest.TestCase):
  def test_add(self):
    self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
  unittest.main()

  #Each test method must start with test_.


#pytest (Popular Third-Party Tool)
#pytest is a modern testing framework that is simpler and more powerful than unittest.
#pytest helps you check whether your code works correctly.

#pip install pytest
#pytest --version
#used in test_math.py & test_calculator.py
#run test - pytest


#Most companies prefer pytest.

#Simple pytest Example
# def add(a, b):
#   return a + b

def test_add():
  assert add(2, 3) == 5
# Running pytest - pytest
#No class needed. Just use assert.
  
'''
unittest vs pytest

unittest	            pytest
Built-in	            Third-party
More boilerplate	    Simple syntax
Class-based	          Function-based

Why pytest is better than unittest?
| Feature             | pytest | unittest |
| ------------------- | ------ | -------- |
| Less code           | ✅      | ❌        |
| Easy syntax         | ✅      | ❌        |
| Better error output | ✅      | ❌        |
| Fixtures support    | ✅      | Limited  |


When should YOU use pytest?

✔ Backend APIs
✔ Automation testing
✔ Data pipelines
✔ Async code (pytest-asyncio)
✔ Interviews & real projects


🔑 Key takeaway : pytest = simple, powerful, industry-standard testing tool

'''
