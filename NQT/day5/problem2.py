# Problem: Find the first "Non-Repeating" character in a string.

s = "aabbcdeeff"

freq ={}
for ch in s:
    freq[ch] = freq.get(ch, 0) +1

for ch in s:
    if freq[ch] == 1:
        print(ch)
        break
    