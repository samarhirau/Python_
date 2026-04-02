# Find All Duplicate Elements in a List
# Write a Python function called find_duplicates that takes a list and returns a new list containing all elements that appear more than once.

def find_duplicates(arr):
    dup = []
    seen = set()
    
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    for ch in freq:
        if freq[ch] > 1 and num not in seen:
            dup.append(ch)
            seen.add(num)
    return dup

arr = [1, 2, 3, 2, 4, 3, 5]
print(find_duplicates(arr))