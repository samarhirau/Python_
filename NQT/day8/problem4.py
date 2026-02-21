# Given an array arr[] and an integer k, rotate the array in place k times to the right (clockwise).

arr = [1, 2, 3, 4, 5]
k = 2
n = len(arr)
k = k % n

# Step 1: Reverse the entire array -> [5, 4, 3, 2, 1]
s, e = 0, n - 1
while s < e:
    arr[s], arr[e] = arr[e], arr[s]
    s, e = s + 1, e - 1

# Step 2: Reverse the first k elements -> [4, 5, 3, 2, 1]
s, e = 0, k - 1
while s < e:
    arr[s], arr[e] = arr[e], arr[s]
    s, e = s + 1, e - 1

# Step 3: Reverse the rest (k to n-1) -> [4, 5, 1, 2, 3]
s, e = k, n - 1
while s < e:
    arr[s], arr[e] = arr[e], arr[s]
    s, e = s + 1, e - 1

print(arr) # Output: [4, 5, 1, 2, 3]