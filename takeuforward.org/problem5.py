# Count frequency of each element in the array

arr = list(map(int , input().split()))


freq = {}

for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)
