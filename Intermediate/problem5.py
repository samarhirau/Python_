# Implement Bubble Sort From Scratch
# Write a Python function called bubble_sort that takes a list and returns it sorted in ascending order using the Bubble Sort algorithm.

def bubble_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print(sorted_arr)