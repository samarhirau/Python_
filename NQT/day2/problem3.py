# Remove Duplicate Characters (Keep Order)

s = input().strip()

arr = []

for i in range(len(s)):
    if s[i] not in arr:
        arr.append(s[i])
result = ''.join(arr)

print(result) 
    
