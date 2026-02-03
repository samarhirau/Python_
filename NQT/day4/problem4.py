# Rotate array RIGHT by K


arr = [1, 2, 3, 4, 5]
k = 2

for _ in range(k):
    last = arr.pop()
    arr.insert(0, last)

print(arr)