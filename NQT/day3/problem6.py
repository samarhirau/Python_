# Question 7: Second Most Frequent Character

s = "aabbcccdd"

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

max_freq = 0
for ch in freq:
    if freq[ch] > max_freq:
        max_freq = freq[ch]

second_max = 0
for ch in freq:
    if freq[ch] != max_freq and freq[ch] > second_max:
        second_max = freq[ch]

for ch in s:
    if freq[ch] == second_max:
        print(ch)
        break
