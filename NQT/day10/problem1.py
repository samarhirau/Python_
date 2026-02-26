# Given an array of integers, find the sum of its elements.


def sum_of_elements(arr):
    total = 0
    for num in arr:
        total += num
        
    return total


arr = [1,2,3,4,5]

print(sum_of_elements(arr))