def find_equilibrium(arr):
    total_sum = sum(arr)
    left_sum = 0
    
    for i in range(len(arr)):
        # Calculate right_sum in O(1)
        right_sum = total_sum - left_sum - arr[i]
        
        if left_sum == right_sum:
            return i
            
        left_sum += arr[i]
        
    return -1

# Test
print(find_equilibrium([1, 3, 5, 2, 2]))