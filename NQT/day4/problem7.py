# Merge Two Sorted Arrays (NO extra array)

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

i = len(arr1) - 1
j = 0

while i >= 0 and j < len(arr2):
    if arr1[i] > arr2[j]:
        arr1[i], arr2[j] = arr2[j], arr1[i]
    i -= 1
    j += 1

arr1.sort()
arr2.sort()

print(*(arr1 + arr2))
