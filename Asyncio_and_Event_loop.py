#1. What is Asyncio?
'''
Asyncio is Python’s library to write concurrent code using the async/await syntax. Useful for I/O-bound tasks like network requests, file operations, or database queries

Asyncio allows tasks to run asynchronously without blocking the main program.

'''
#Event Loop
'''
Event loop manages and schedules asynchronous tasks in asyncio.


'''
import asyncio
import aiohttp #pip install aiohttp

async def say_hello():
  print("Hello")

asyncio.run(say_hello())
#asyncio.run() starts the event loop and executes the coroutine.


#Async Functions
async def greet(name):
  await asyncio.sleep(1)
  print(f"Hello {name}")

async def main():
  await asyncio.gather(greet("Bhavesh"), greet("Alice"))

asyncio.run(main())
#await pauses coroutine until the awaited task completes.


#asyncio.gather
#Runs multiple coroutines concurrently.

async def task1():
  await asyncio.sleep(1)
  print("Task 1 done")

async def task2():
  await asyncio.sleep(2)
  print("Task 2 done")

async def main():
  await asyncio.gather(task1(), task2())

asyncio.run(main())
#Both tasks run concurrently, saving total execution time.

'''
asyncio.sleep vs time.sleep
Function	         Behavior
time.sleep()	     Blocks the whole program
asyncio.sleep()	   Non-blocking, allows other tasks to run
'''

#6. Practical Example – Fetch URLs

async def fetch(url):
  async with aiohttp.ClientSession() as session:
    async with session.get(url) as resp:
      print(await resp.text())

asyncio.run(fetch("https://example.com"))
#Shows async network requests using aiohttp library.

'''
 Key Tips
Use asyncio for I/O-bound tasks, not CPU-bound
Always await coroutines
Use asyncio.gather() to run multiple coroutines concurrently
Do not mix blocking code inside async functions

'''