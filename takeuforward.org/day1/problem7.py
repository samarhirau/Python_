# Calculate Sum of the Elements of the Array

arr = list(map(int, input().split()))

sum = 0

for i in range(len(arr)):
    sum = arr[i] + sum 
    
print(sum)