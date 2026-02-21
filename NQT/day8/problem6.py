# Reverse an array arr[]. Reversing an array means rearranging the elements such that the first element becomes the last, the second element becomes second last and so on.

arr = [1, 2, 3, 4, 5]
n = len(arr)

left = 0
right = n - 1

while left < right:
    # Swap elements at left and right
    arr[left], arr[right] = arr[right], arr[left]
    
    # Move pointers toward the middle
    left += 1
    right -= 1

print(arr) 