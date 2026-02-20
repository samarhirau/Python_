# Find the first non-repeating element in a given array arr of integers and if there is not present any non-repeating element then return 0
arr = [-1, 2, -1, 3, 2]

freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1
            
for i in range(len(arr)):
    if freq[arr[i]] == 1:
        print(arr[i])
        break
else:
    print(0)


   