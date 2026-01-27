# Find Median of the given Array

arr = sorted(list(map(int, input().split())))

n = len(arr)

if n % 2 == 1:
    median = arr[n // 2]
else:
    # If length is even, median is the average of two middle elements
    median = (arr[n // 2 - 1] + arr[n // 2]) / 2

print(f"Median: {median}")


