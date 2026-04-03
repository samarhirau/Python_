# Find the Intersection of Two Lists
# Write a Python function called intersection that takes two lists and returns a new list containing only the elements that appear in both lists.


def intersection(arr1, arr2):
    if not arr1 or not arr2:
        return []
    
    seen = set()
    result = []
    set2 = set(arr2)  # O(1) lookup ✅
    
    for num in arr1:
        if num in set2 and num not in seen:  # O(1) lookup! ✅
            seen.add(num)
            result.append(num)
    
    return result

a = [1, 1, 2, 3]
b = [1, 2, 2, 4]
print(intersection(a, b))  