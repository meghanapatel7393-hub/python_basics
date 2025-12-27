#1. What is an Iterator?

'''
An iterator is an object that allows traversal through elements one at a time.

Uses __iter__()
Uses __next__()
'''

nums = [1, 2, 3]
it = iter(nums)
print(next(it))
print(next(it))
'''
Interview line:
“Iterator remembers its state while iterating.”

Iterable vs Iterator

Iterable	          |  Iterator
Can be looped over	|  Returns one value at a time
Has __iter__()	    |  Has __iter__() and __next__()
Example: list,      |  tuple	Example: iter(list)

'''

# What is a Generator?
#A generator is a special function that returns an iterator using yield.

def count_up(n):
  for i in range(n):
    yield i
g = count_up(3)
print(next(g))
print(next(g))
#Generator pauses execution and resumes later.
'''
yield vs return

yield	                            |  return
Returns value and pauses	        | Ends function execution
Multiple yields possible	        | Only one return
Memory efficient	Returns         | entire result
'''

#Generator Expression
gen = (x*x for x in range(5))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
#Similar to list comprehension but lazy execution.

#Memory Efficiency
# List
nums = [x for x in range(1000000)]
# Generator
nums = (x for x in range(1000000))

#Generators use significantly less memory.
