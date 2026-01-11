# Problem 9: Set Mutations
""" You are given a set  and  other sets. Your task is to perform  operations
on set  and print the sum of its elements.
"""

num_setA = int(input())
setA = set(map(int, input().split()))

num_operations = int(input())

for _ in range(num_operations):
    op_name, _ = input().split()
    setB = set(map(int, input().split()))

    if op_name == "intersection_update":
        setA.intersection_update(setB)
    elif op_name == "symmetric_difference_update":
        setA.symmetric_difference_update(setB)
    elif op_name == "difference_update":
        setA.difference_update(setB)
    elif op_name == "update":
        setA.update(setB)

print(sum(setA))
