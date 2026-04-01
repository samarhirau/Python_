# Find the Missing Number in a List
# Write a Python function called find_missing that takes a list of integers from 1 to n with one number missing and returns the missing number.


def find_missing(arr):
    n = len(arr) + 1
    arr_sum = sum(arr)
    actual_sum = n * (n +1) // 2
    
    return ( actual_sum - arr_sum )


arr =  [1, 2, 3, 4, 6, 7, 8, 9, 10]
print(find_missing(arr))
