# Sort Elements of an Array by Frequency

array = [1,2,3,2,4,3,1,2]

sorted_array = sorted(array)

frequency = {}
for num in sorted_array:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
sorted_by_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
result = []
for num, freq in sorted_by_frequency:
    result.extend([num] * freq)
print(result)  