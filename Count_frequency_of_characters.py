#Method 1: Using a Dictionary (Best for learning basics)
text = "hello"

freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)


#Method 2: Using dict.get() (Cleaner & recommended)
text = "hello"
freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)


#Method 3: Using collections.Counter (Pythonic & shortest)
from collections import Counter

text = "hello"
freq = Counter(text)

print(freq)

'''
⚠️ Best for real projects, but learn dictionary method first since you’re a fresher.
'''

#Method 4: Count frequency ignoring spaces
text = "hello world"
freq = {}

for ch in text:
    if ch != " ":
        freq[ch] = freq.get(ch, 0) + 1

print(freq)
