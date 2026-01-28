# Find all repeating elements in an array

arr = [1,1,2,3,4,4,5,2]

arr.sort()
re_arr = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j] and arr[i] not in re_arr:
            re_arr.append(arr[i])
        
print(re_arr)