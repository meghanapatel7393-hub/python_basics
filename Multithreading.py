#1. Why Multithreading?
#Multithreading allows Python to run multiple threads (tasks) concurrently, useful for I/O bound tasks.
#Threads share memory space but may need synchronization for shared data.

import threading
from multiprocessing import Process

def print_numbers():
  for i in range(5):
    print(i)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_numbers)

t1.start()
t2.start()

t1.join()
t2.join()
#start() begins the thread, join() waits for completion.

print("Thread Synchronization")
#Thread Synchronization
counter = 0
lock = threading.Lock()

def increment():
  global counter
  for _ in range(1000):
    with lock:
      counter += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print("Counter:", counter)
'''
counter → a global variable that will be incremented.

lock → a threading lock, used to prevent multiple threads from changing counter at the same time.

Loops 1000 times.

with lock: → acquires the lock before modifying counter and releases it automatically after.

This prevents race conditions, where multiple threads try to update the variable simultaneously, which can give wrong results.

t1 and t2 are two separate threads running the same increment() function.

start() → runs the thread in parallel.

join() → waits for the thread to finish before moving on.

Both threads incremented counter 1000 times each → total = 2000.

Because we used a lock, we avoid the race condition.

Without the lock, the threads could interfere and the counter might be less than 2000 because both threads read and write counter at the same time.

| Concept                   | Explanation                                                        |
| ------------------------- | ------------------------------------------------------------------ |
| `threading.Thread`        | Creates a new thread of execution                                  |
| `lock = threading.Lock()` | Prevents multiple threads from changing shared data simultaneously |
| `with lock:`              | Safely acquires and releases the lock around critical code         |
| `counter += 1`            | Critical section that must be protected to avoid race conditions   |
| `join()`                  | Waits for the thread to finish                                     |


KEY POINT : Whenever multiple threads modify the same variable, you should use a lock to ensure data integrity.
'''
#Locks prevent race conditions in shared resources.

#Multiprocessing
#Multiprocessing runs multiple processes in parallel, bypassing Python’s GIL, useful for CPU-bound tasks.





def print_numbers():
  for i in range(5):
    print(i)

'''
On Windows, Python cannot safely start a new process unless the process creation code is protected by:

if __name__ == "__main__":
for any multiprocessing code, especially on Windows.

Unlike Linux/macOS (which use fork), Windows uses spawn to start new processes.

If you don’t use if __name__ == "__main__":, Python tries to re-import your script to start the new process. This leads to recursive process creation and eventually the error:

RuntimeError: An attempt has been made to start a new process before the current process has finished its bootstrapping phase.

'''

if __name__ == "__main__": #On Windows, Python cannot safely start a new process unless the process creation code is protected by: without this line code not work in window
  p1 = Process(target=print_numbers)
  p2 = Process(target=print_numbers)

  p1.start()
  p2.start()

  p1.join()
  p2.join()
#Each process has its own memory space.
#This tells Python: “Only run this code when the script is executed directly, not when imported.”
