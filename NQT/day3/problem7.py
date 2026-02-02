# Question 8: First Repeating Character

s = "abcaabcd"

freq = {}

for ch in s:
    if ch in freq:
        print(ch)
        break
    else:
        freq[ch] = 1
else:
    print(-1)
