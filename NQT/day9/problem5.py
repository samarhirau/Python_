# Given an array arr[] of non-negative integers which may contain duplicate elements. Return the frequency of each distinct element present in the array.


def count_frequency(arr):
    freq = {}
    
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    
    return freq

arr = [22, 11, 33, 1, 5, 8, 11, 89, 9]
print(count_frequency(arr))