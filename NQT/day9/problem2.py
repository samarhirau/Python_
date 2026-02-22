# Find the smallest and second smallest elements in an array

def find_small(arr):
    small = float('inf')
    second_small = float('inf')
    
    for num in arr:
        if num < small:
            second_small = small
            small = num
        elif num < second_small and num != small:
            second_small = num
            
    return small, second_small


    
    
    
arr = [1, 2, 1 , 2, 34,34,3 , 43]
print(find_small(arr))