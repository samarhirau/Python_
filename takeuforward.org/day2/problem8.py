# Replace elements by its rank in the array

arr = [40, 10, 20, 30]


sorted_arr = sorted(arr)

rank_arr = []
for x in arr:
    rank_arr.append(sorted_arr.index(x) + 1)

print(rank_arr)