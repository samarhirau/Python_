# Given an array of integers arr[], sort the array according to the frequency of elements, i.e. elements that have higher frequency comes first. If the frequencies of two elements are the same, then the smaller number comes first.


def frequency_sort(arr):
    freq = {}
    arr.sort()
    
    for num in arr:
        freq[num] = freq.get(num,  0) + 1
    
    sorted_arr = sorted(arr, key=lambda x: (-freq[x], x))
    return sorted_arr


arr = [2,2,4,4,1,1,1]
print(frequency_sort(arr))
        
    