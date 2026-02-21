# Given an array arr[] of size n, find an equilibrium index (if any) or -1 if no equilibrium index exists.

# arr = [-7, 1, 5, 2, -4, 3, 0]
# n = len(arr)

def equilibrium_index(arr):
    total = sum(arr)
    left_sum = 0
    
    for i in range(len(arr)):
        
        right_sum = total - left_sum - arr[i]
        
        if right_sum == left_sum:
            return i 
        
        left_sum = left_sum + arr[i]
        
    return -1

arr = [-7, 1, 5, 2, -4, 3, 0]
print(equilibrium_index(arr))