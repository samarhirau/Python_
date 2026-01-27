# Rearrange array in increasing-decreasing order

arr = sorted(list(map(int, input().split())))


arr1 = []
stop = int(len(arr))
for i in range( int(stop/2)):
    arr1.append(arr[i])
    
for j in range(stop-1, int((stop/2)-1), -1):
    arr1.append(arr[j])
    
print(arr1)
    