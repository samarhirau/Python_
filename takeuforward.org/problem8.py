# Rotate array by K elements : Block Swap Algorithm

N = int(input())
arr = list(map(int, input().split()))
k = int(input())


for i in range(k):
    first = arr[0]
    arr.pop(0)
    arr.append(first)

print(arr)