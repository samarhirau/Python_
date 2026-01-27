# Find Second Smallest and Second Largest Element in an array

arr = list(map(int, input().split()))

sorted_arr = sorted(set(arr))  # use set because numbers repeated in arr

print(sorted_arr[2])
print(sorted_arr[-2])