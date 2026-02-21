# Check if an array is subset of another array

arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]

# Step 1: Build a frequency map for the main array
freq = {}
for num in arr1:
    freq[num] = freq.get(num, 0) + 1

# Step 2: Check elements of the potential subset
is_subset = True
for num in arr2:
    if num in freq and freq[num] > 0:
        # Subtract count to handle duplicate elements correctly
        freq[num] -= 1
    else:
        is_subset = False
        break

if is_subset:
    print("Yes")
else:
    print("No")