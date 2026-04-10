# Implement Binary Search
# Write a Python function called binary_search that takes a sorted list and a target value and returns the index of the target if found, otherwise returns -1.


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

sorted_list = [1, 2, 3, 4, 5,6, 7, 8, 9, 10]
target_value = 5
result = binary_search(sorted_list, target_value)
print(result)  