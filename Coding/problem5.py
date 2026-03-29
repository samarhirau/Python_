# Count the Frequency of Each Character in a String

def count_freq(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch , 0) + 1

    return freq

s = "Hello Wolrd"
print(count_freq(s))