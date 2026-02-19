
# Problem: "Subarray with Given Sum"
# Given an array of non-negative integers and a target sum, find a contiguous subarray that adds up to that sum. Return the starting and ending indices (1-based indexing). If no such subarray exists, return -1.

arr = [1, 2, 3, 7, 5]
target = 12

def find_subarray_with_sum(arr, target):
    current_sum = 0
    start = 0
    
    for end in range(len(arr)):
        current_sum += arr[end]
        
        while current_sum > target and start < end:
            current_sum -= arr[start]
            start += 1
            
        if current_sum == target:
            return (start + 1, end + 1)  
            
    return -1   
result = find_subarray_with_sum(arr, target)
print(result)