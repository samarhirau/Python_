# Given an array of positive integers arr[] of size n, the task is to find second largest distinct element in the array.

def find_secondLarge(arr):
    if len(arr) < 2:
        return None 
    
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in arr:
        if num > largest:
            # Purana largest ab second largest ban jayega
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            # Agar num largest se chota hai par second_largest se bada
            second_largest = num
            
    return second_largest if second_largest != float('-inf') else None


arr = [22, 11, 33, 1, 5, 8, 11, 89, 9]
print(find_secondLarge(arr))