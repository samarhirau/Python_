def twoSum( arr, target):
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False

# Example usage:
arr = [10, 15, 3, 7]
target = 17
print(twoSum( arr, target))  # Output: True