# Find the Subarray with Maximum Sum (Kadane's Algorithm)
# Write a Python function called max_subarray_sum that takes a list of integers and returns the maximum sum of any contiguous subarray.

def max_subarray_sum(arr):
    if not arr:
        return 0

    max_sum = float('-inf')  
    current_sum = 0  

    for num in arr:
        current_sum += num  
        if current_sum > max_sum:
            max_sum = current_sum  

        if current_sum < 0:
            current_sum = 0  

    return max_sum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(arr)
print(result)
