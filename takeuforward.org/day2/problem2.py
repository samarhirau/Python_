# Remove Duplicates in-place From an Unsorted Array

arr = [1 , 7, 5, 7, 3,6, 4,3 ,6,7 ,344, 77,33, 1, 1, 7 ,11 ]

arr.sort()
len_arr = len(arr)
set_arr = set(arr)
arr = list(set_arr)
arr.sort()

for i in range(len_arr - len(arr)):
    arr.append('_')
    
print(arr)