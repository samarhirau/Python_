# Given an array of integers, move all Even numbers to the beginning and all Odd numbers to the end. The relative order of even numbers doesn't matter here, but you must do it in-place (don't create a new array).


arr = [3, 1, 2, 4, 7, 8]

j = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0:
       # Swap elements
        arr[i], arr[j] = arr[j], arr[i]
        j += 1
        
print(arr)