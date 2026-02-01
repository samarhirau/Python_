# Problem: Find Second Smallest Element


arr = list(map(int, input().split()))

unique = list(set(arr))
unique.sort()

print(unique[1])

