# Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.



def rotate_left(arr, d):
    n = len(arr)
    # 1. Handle cases where d is larger than array length
    d = d % n 
    
    # Helper function to reverse a portion of the array
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # 2. Reverse the first 'd' elements
    reverse(0, d - 1)
    
    # 3. Reverse the rest of the elements (from d to end)
    reverse(d, n - 1)
    
    # 4. Reverse the entire array
    reverse(0, n - 1)   

# Example Usage
arr = [1, 2, 3, 4, 5]
d = 2
rotate_left(arr, d)
