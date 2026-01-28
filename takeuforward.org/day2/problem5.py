# Find all the non-repeating elements in an array
arr = [1, 1, 2, 3, 4, 4, 5, 2]

seen = set()
repeated = set()

for num in arr:
    if num in seen:
        repeated.add(num)
    else:
        seen.add(num)

print(list(seen - repeated))
