# multithreading_multiprocessing.py

import threading
from multiprocessing import Process

# -------------------------------
# THREADING EXAMPLE
# -------------------------------

def print_numbers_thread():
    """Print numbers 0-4 (Threading example)"""
    for i in range(5):
        print(i)

def threading_example():
    print("Starting Threading Example...\n")

    t1 = threading.Thread(target=print_numbers_thread)
    t2 = threading.Thread(target=print_numbers_thread)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Thread Synchronization Example Completed\n")

# Shared counter for threading example
counter = 0
lock = threading.Lock()

def increment_counter():
    """Increment the global counter safely using a lock"""
    global counter
    for _ in range(1000):
        with lock:
            counter += 1

def threading_counter_example():
    print("Starting Counter Increment with Threads...\n")

    t1 = threading.Thread(target=increment_counter)
    t2 = threading.Thread(target=increment_counter)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Final Counter Value (Threads):", counter, "\n")

# -------------------------------
# MULTIPROCESSING EXAMPLE
# -------------------------------

def print_numbers_process():
    """Print numbers 0-4 (Multiprocessing example)"""
    for i in range(5):
        print(i)

def multiprocessing_example():
    print("Starting Multiprocessing Example...\n")

    p1 = Process(target=print_numbers_process)
    p2 = Process(target=print_numbers_process)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Multiprocessing Example Completed\n")

# -------------------------------
# MAIN EXECUTION
# -------------------------------
if __name__ == "__main__":
    # Threading demos
    threading_example()
    threading_counter_example()

    # Multiprocessing demo
    multiprocessing_example()

'''
Key points

if __name__ == "__main__":

Required for multiprocessing on Windows to avoid recursive process spawning.

Threading

Threads share memory, so a Lock is used to prevent race conditions.

Multiprocessing

Processes do not share memory. Each process runs independently.

Output

Thread numbers may interleave in output.

Counter with lock always prints 2000.

Multiprocessing numbers also may interleave.
'''