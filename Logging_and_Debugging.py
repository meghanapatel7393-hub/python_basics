#Why Logging?
#Logging helps record events and debug information instead of using print(). It’s better for production-ready applications.

#  Basic Logging Setup
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
logging.warning("This is a warning")
logging.error("This is an error")

#Logging to a File
logging.basicConfig(filename="app.log", level=logging.INFO,
format='%(asctime)s:%(levelname)s:%(message)s')
logging.info("Application started")
logging.error("An error occurred")
#Logs can now be saved to a file with timestamps and levels.

#Debugging with pdb
#Python debugger (pdb) allows step-by-step execution to find bugs.


import pdb

def add(a, b):
  return a + b

pdb.set_trace() # Start debugger
result = add(5, 7)
print(result)
#Use commands: n (next), c (continue), l (list), p (print variable)
