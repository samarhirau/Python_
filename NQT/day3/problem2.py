# First Non-Repeating Character

s = "aabbccdd"

freq = {}

for ch in s:
    if not ch in freq:
        freq[ch] = 1
    else:
        freq[ch] += 1

for ch in freq:
    if freq[ch] == 1:
        print(ch)        
        break
else:
    print(-1)