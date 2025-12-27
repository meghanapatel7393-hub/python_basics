# for loop with else
for i in range(1, 4):
    print(i)
else:
    print("else block")

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

n=int(input("enter a number : "))
for i in range(1,n+1):
    print("*"*i)
    
print("\n same start print as above")    
#same start print as above
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()

print("\n reverse")
# reverse print as above
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print("*",end="")
    print()

s=input("enter a string : ")
for i in s:
    print(i)    

for i in s:
    print(i,end="")    

print("\n reverse")
s=s[::-1]
print(s)    

'''
    *
   ***
  *****
 *******
********* 
'''

for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end="")
    print()

'''
*********
 *******
  *****
   ***
    *
'''
print("\n reverse")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(" ",end="")
    for k in range(1,2*(n+1-i)):
        print("*",end="")
    print()    


print("same above other way")
'''
    *
   ***
  *****
 *******
*********
'''
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1))

'''
*********
 *******
  *****
   ***
    *
'''
print("\n reverse")
for i in range(1,n+1):
    print(" "*(i-1),end="")
    print("*"*(2*(n+1-i)-1))


'''
****
*  *
*  *
*  *
****
'''

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()



print("\n same above otehr way")
# First row
print("*" * n)

# Middle rows
for i in range(n - 2):
    print("*" + " " * (n - 2) + "*")

# Last row
print("*" * n)


print("\n same above otehr way Using join()")
for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * n)
    else:
        print("*" + " ".join([""] * (n - 1)) + "*")


print("\n same above otehr way Using List Comprehension")
for i in range(n):
    row = ["*" if i == 0 or i == n-1 or j == 0 or j == n-1 else " "
           for j in range(n)]
    print("".join(row))        

print("\n same above otehr way Using Strings Only (Fast)") 

middle = "*" + " " * (n - 2) + "*"

print("*" * n)
for _ in range(n - 2):
    print(middle)
print("*" * n)


#here n**0.5 is square root of n its used to check prime or not and enoght to check prime or not like 9**0.5 is 3.0
'''
Example: n = 36
Factor pairs:
1 × 36
2 × 18
3 × 12
4 × 9
6 × 6  ← √36


After 6, factors repeat in reverse:
9 × 4
12 × 3

So checking beyond √n is useless.
'''
if n<2:
    print("Not Prime")
else:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print("Not Prime")
            break
    else:
        print("Prime")


print("\n other way to check no is prime or not")
if n <= 1:
    print("Not Prime")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")

