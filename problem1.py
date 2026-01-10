# Print the different combinations of string S on separate lines.


from itertools import combinations

s, num = input().split()
k = int(num)


for p in combinations(sorted(s), k):
    
    print(''.join(p))