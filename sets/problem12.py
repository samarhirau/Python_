# problem12 : Check if a set is a strict superset of other sets
'''
You are given a set A and n other sets. Your task is to find whether set A is a strict superset of each of the n sets.
Input Format:
The first line contains the space-separated elements of set A.
The second line contains integer n, the number of other sets.
The next n lines contains the space-separated elements of each other set.
'''


setA = set(map(int, input().split()))
n = int(input())
is_strict_superset = True

for _ in range(n):
    setB = set(map(int, input().split()))
    if not (setA.issuperset(setB) and setA != setB):
        is_strict_superset = False
        break

print(is_strict_superset)