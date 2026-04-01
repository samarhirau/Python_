# Find the Most Frequent Element in a List
# Write a Python function called most_frequent that takes a list and returns the most frequent element in it.


def most_frequent(arr):
    freq = {}
    
    for ch in arr:
        freq[ch] = freq.get(ch, 0) + 1
    
    return max(freq, key=freq.get)

arr =[1, 1, 2, 2, 3]
print(most_frequent(arr))