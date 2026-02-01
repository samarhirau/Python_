# Problem: Find First Repeating Character

s= input().strip()

freq = {}
seen = ''

for ch in s:
    if not ch in freq:
        freq[ch] = 1
    else:
        freq[ch] += 1
        if freq[ch] == 2:
            seen = ch
            break
else:
    print(-1)

