# Find the Longest Consecutive Sequence
# Write a Python function called longest_consecutive that takes a list of integers and returns the length of the longest consecutive sequence.


def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Check if it's the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            # Count the length of the consecutive sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            longest = max(longest, current_length)

    return longest

a = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(a))
