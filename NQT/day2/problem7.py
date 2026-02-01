# Problem: Rotate Array Left by K Positions

arr = list(map(int, input().split()))
k = int(input())

k = k % len(arr)

print(k)

for _ in range(k):
    first = arr.pop(0)
    arr.append(first)

print(*arr)
