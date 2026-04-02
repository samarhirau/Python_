# Rotate a List by K Positions
# Write a Python function called rotate_list that takes a list and a number k and returns the list rotated to the right by k positions.


def rotate_list(arr, k):
    if not arr:
        return []
    
    k = k % len(arr)  
    
    for _ in range(k):
        last = arr.pop()     
        arr.insert(0, last)   
    
    return arr

arr = [1, 2, 3, 4, 5]
k = 2
print(rotate_list(arr, k)) 

