# Rotate array by K elements

arr = [1, 2, 3, 4, 5, 6, 7]
k = int(input()) 
rotate = input()

for i in range(k):
    if rotate == 'left':
        arr.append(arr[0])
        arr.pop(0)
    else:
        arr.insert(0,arr[-1])
        arr.pop()
        
print(arr)