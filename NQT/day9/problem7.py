# Given a sorted array arr[] of size n, the goal is to rearrange the array so that all distinct elements appear at the beginning in sorted order. Additionally, return the length of this distinct sorted subarray.


def removeDuplicates(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result



arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
print(removeDuplicates(arr))