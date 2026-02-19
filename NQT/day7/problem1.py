# Problem: "Equilibrium Index"
# Find the index such that the sum of elements at lower indices is equal to the sum of elements at higher indices.

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