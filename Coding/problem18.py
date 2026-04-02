# Merge Two Sorted Lists Without Using sort()
# Write a Python function called merge_sorted that takes two sorted lists and returns a single sorted merged list without using sort() or sorted().


def merge_sorted(arr1, arr2):
    if len(arr1) == 0 and len(arr2) == 0:
        return []
    merged = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    return merged

arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(merge_sorted(arr1, arr2))

    