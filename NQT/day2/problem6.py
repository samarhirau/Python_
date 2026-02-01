# Problem: Sort Array Without Built-in Sort

arr = list(map(int , input().split()))


sort_arr = []

while len(arr) > 0:
    min_val = arr[0]
    for val in arr:
        if val < min_val:
            min_val = val
    sort_arr.append(min_val)
    arr.remove(min_val)
    
    
print(*sort_arr)
         