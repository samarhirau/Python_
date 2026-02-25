# Given an array arr[], check if it is sorted in ascending order or not. Equal values are allowed in an array and two consecutive equal values are considered sorted.



def is_sorted(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return True
    
    
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False
            
    return True
        
    
arr = [10,20,30,30,50]
print(is_sorted(arr))