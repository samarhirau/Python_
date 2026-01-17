# Problem 4: itertools.combinations_with_replacement()
# Print the different combinations of string S on separate lines.

from itertools import combinations_with_replacement

s, num = input().split()
k = int(num)


for p in combinations_with_replacement(sorted(s), k):
    print(''.join(p))