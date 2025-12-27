#Used to read/write data in files.

#Open a File - need to create data.txt manually
file = open("data.txt", "r")

'''
File Modes:
| Mode    | Meaning           |
| ------- | ----------------- |
| r       | read              |
| w       | write (overwrite) |
| a       | append            |
| x       | create            |
| rb / wb | binary            |

'''

# Read File
file = open("data.txt", "r")
print(file.read())
file.close()


#Read line by line:
file = open("data.txt", "r")
print(file.readline())
file.close()


#Write File
file = open("data.txt", "w")
file.write("Hello Python")
file.close()

#Append:
file = open("data.txt", "a")
file.write("\nNew Line Added")
file.close()

#Best Way: with Statement
#Automatically closes file.
with open("data.txt", "r") as file:
    print(file.read())


#Exception Handling
#Used to handle errors without crashing program.
#Simple Try-Except
try:
    x = int(input("Enter number: "))
    print(10 / x)
except:
    print("Something went wrong")

#Specific Exception
try:
    x = int(input("Enter number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")



#Multiple Exceptions
try:
    x = int(input("Enter number: "))
    print(10 / x)
except (ValueError, ZeroDivisionError):
    print("Please enter a number greater than 0") 


#Multiple Exceptions
try:
    x = int(input("Enter number: "))
    print(10 / x)
except ValueError:
    print("Please enter a number")
except ZeroDivisionError:
    print("Please enter a number greater than 0") 
except:
    print("Something went wrong")


try:
    print("No error")
except:
    print("Error")
else:
    print("Success")
finally:
    print("Always runs")
    
