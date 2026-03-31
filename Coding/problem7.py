# Find All Pairs That Sum to a Target
# Write a Python function called find_pairs that takes a list of numbers and a target sum as input and returns all unique pairs that add up to the target.


def find_pairs(numbers, target):
    seen = set()
    pairs = set()
    for num in numbers:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)
    return list(pairs)


numbers = [1, 2, 3, 4, 5, 6]
target = 7
result = find_pairs(numbers, target)
print(result)  