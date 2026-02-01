# Problem: Find Missing Number

# You are given n-1 numbers from 1 to n.
# Find the missing number.


arr = list(map(int, input().split()))


n = len(arr) + 1
total = n * (n + 1) // 2
missing_number = total - sum(arr)
print(missing_number)
