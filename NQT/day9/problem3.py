# Given an arr[] of elements of size n, return the largest element given in the array.

def find_large(arr):
    if not arr: 
        return 0
    
    largest = arr[0]
    
    for num in arr:
        if num > largest:
            largest = num
    
    return largest


arr = [22, 11 , 33, 1, 5, 8, 11, 89, 9]
print(find_large(arr))