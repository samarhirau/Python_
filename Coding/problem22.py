# Find the Union of Two Lists
# Write a Python function called union that takes two lists and returns a new list containing all unique elements from both lists.


def union(arr1, arr2):
    seen = set()
    result = []
    
    for num in arr1:
        if num not in seen:
            seen.add(num)
            result.append(num)
            
    for num in arr2:
        if num not in seen:
            seen.add(num)
            result.append(num)
            
    return result 
a = [1, 1, 2, 3]
b = [1, 2, 2, 4]
print(union(a, b))  
    
    