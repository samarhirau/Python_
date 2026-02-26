# Program for average of an array (Iterative and Recursive)

def find_avg(arr):
    sum = 0
    for num in arr:
        sum += num
        
    return sum // len(arr)

arr = [1, 2, 3, 4, 5]
print(find_avg(arr))