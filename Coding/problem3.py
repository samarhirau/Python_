# Find the Second Largest Number in a List

def second_largest(arr):
    first = second = float('-inf')
    
    for num in arr:
        if num > first:
            second = first
            first = num 
        elif num != first and num > second:
            second = num 
            
    if second == float('-inf'):
        return None  # all elements were same
            
    return second
        
    
arr = [1,2,3,4,5,6,7,8,9,0]
res = second_largest(arr)
print(res)
    