
'''
Basic Patterns
abc – Matches literal "abc"
^ – Start of string
$ – End of string
. – Any character except newline
* – 0 or more repetitions
+ – 1 or more repetitions
? – 0 or 1 repetition
[a-z] – Any lowercase letter
'''
#this 2 line in multicomment s given me warning so it keep seperate
#  \d – Digit (0-9)
#  \w – Word character (a-z, A-Z, 0-9, _)

import re
pattern = r"\d+" # Matches 1 or more digits  #r stands for raw string.
text = "My number is 12345"
result = re.findall(pattern, text)
print(result) # Output: ['12345']
# Email validation
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"  #r stands for raw string. It tells Python: “Take this string exactly as it is, don’t treat backslashes \ as escape characters.”
text = "test@example.com"
if re.match(pattern, text):
  print("Valid email")
else:
  print("Invalid email")


  #Compiling Patterns
pattern = re.compile(r"\d+") #r stands for raw string.
result = pattern.findall("There are 12 cats and 5 dogs")
print(result) # ['12', '5']
#Compiling improves performance if pattern is used multiple times.

'''
What r means

r stands for raw string.

It tells Python: “Take this string exactly as it is, don’t treat backslashes \ as escape characters.”

2️⃣ Why it’s needed for regex
In regex, we often use backslashes, e.g.,

| Regex | Meaning                               |
| ----- | ------------------------------------- |
| `\d`  | Any digit (0-9)                       |
| `\w`  | Any word character (a-z, A-Z, 0-9, _) |
| `\s`  | Any whitespace (space, tab)           |

here compiler given warning of \ used in this comments so ignor it


pattern = "\d+"  # ❌ Not raw
pattern = r"\d+"  # ✅ Raw string
Python passes the string to the regex engine exactly as \d+, which is what we want.
'''