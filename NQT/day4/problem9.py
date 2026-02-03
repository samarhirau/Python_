# Number of ranks cut in the list

n = 6
arr = [4, 3, 7, 2, 6, 1]

count = 0

for i in range(1,n):
    if arr[i] < arr[i -1]:
        count += 1

print(count)
