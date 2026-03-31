# Flatten a Nested List
# Write a Python function called flatten that takes a nested list as input and returns a single flat list with all the elements.

def flatten(arr):
    res = []
    for item in arr:
        if isinstance(item, list): 
            res.extend(flatten(item))
        else:
            res.append(item)
    return res

arr = [1, [2, 3], [4, [5, 6]], 7]
print(flatten(arr))




# ToolUseisinstance(x, list)
# Check if x is a list isinstance(x, int)
# Check if x is an integerisinstance(x, str)
# Check if x is a stringtype(x) == listAlternative but less preferred