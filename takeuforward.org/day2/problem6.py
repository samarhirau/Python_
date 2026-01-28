# Find all Symmetric Pairs in the array of pairs

arr = [(1, 2), (2, 1), (3, 4), (4, 5), (5, 4)] 

res = []
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i][0] == arr[j][1] and arr[i][1] == arr[j][0]:
            res.append((arr[i], arr[j]))
     
            
            
print(res)