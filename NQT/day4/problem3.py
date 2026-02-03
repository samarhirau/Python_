# First Non-Repeating Character

s = "swiss"

freq = {}

for ch in s:
    freq[ch] = freq.get(ch , 0 ) + 1

for i in freq:
    if freq[i] == 1:
        print(i)
        break
else:
    print(-1)