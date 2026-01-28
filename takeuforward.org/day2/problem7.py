# Maximum Product Subarray in an Array

arr = [1,2,-3,0,-4,-5]

max_prod = 1
min_prod = 1
result = 0   # ensures positive output

for num in arr:
    if num == 0:
        max_prod = 1
        min_prod = 1
        continue

    temp = max_prod * num
    max_prod = max(num, temp, min_prod * num)
    min_prod = min(num, temp, min_prod * num)

    if max_prod > 0:
        result = max(result, max_prod)

print(result)
