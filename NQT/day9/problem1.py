def find_mean(arr):
    if not arr: return 0
    
    return sum(arr) // len(arr)

def find_median(arr):
    n = len(arr)
    if n == 0: return 0
    
    
    arr.sort()
    
    if n % 2 == 0:
        
        return (arr[(n // 2) - 1] + arr[n // 2]) / 2
    else:
        
        return arr[n // 2]



arr = [1, 2, 19, 28, 5]
print(find_mean(arr))
print(find_median(arr))