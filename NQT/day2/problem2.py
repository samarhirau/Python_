# Count Frequency of Each Character
s = input().strip()

freq = {}


for ch in s:
    if ch not in freq:
        freq[ch] = 1
    else:
        freq[ch] += 1



for ch in freq:
    print(ch , freq[ch])