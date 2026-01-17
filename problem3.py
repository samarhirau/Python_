
from itertools import combinations


s, num = input().split()
k = int(num)


for i in range(1, k+1):
    for p in combinations(sorted(s), i):
        print(''.join(p))