arr = [1, 3, 5, 2, 2]

left_sum = 0
total_sum = sum(arr)

for i in range(len(arr)):
    # Calculate right_sum in O(1)
    right_sum = total_sum - left_sum - arr[i]
    
    if left_sum == right_sum:
        print(i)
        break
        
    left_sum += arr[i]
    
print(-1)
