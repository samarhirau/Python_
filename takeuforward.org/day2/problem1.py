# Remove Duplicates in-place from Sorted Array

arr = [0,0,1,1,1,2,2,3,3,4]

set_arr = set(arr)

arr = list(set_arr)
arr.sort()
print(arr)