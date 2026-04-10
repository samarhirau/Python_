# Find the Missing and Duplicate Number in a List
# Write a Python function called find_missing_duplicate that takes a list of integers from 1 to n where one number is missing and one number is duplicated. Return both numbers as a tuple (duplicate, missing).

def find_missing_duplicate(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    expected_sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
    
    actual_sum = sum(nums)
    actual_sum_of_squares = sum(x**2 for x in nums)
    
    sum_diff = expected_sum - actual_sum
    square_sum_diff = expected_sum_of_squares - actual_sum_of_squares
    
    missing_plus_duplicate = square_sum_diff // sum_diff
    
    duplicate = (missing_plus_duplicate - sum_diff) // 2
    missing = duplicate + sum_diff
    
    return (duplicate, missing)

# Example usage:
nums = [1, 2, 2, 4]
result = find_missing_duplicate(nums)
print(result) 