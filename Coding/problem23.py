# Check if a List is Sorted
# Write a Python function called is_sorted that takes a list and returns True if the list is sorted in ascending order, otherwise False.

    
def is_sorted(arr):
    if len(arr) <= 1:
        return True
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True

a = [1, 1, 1,2, 3, 4]
print(is_sorted(a))  
        