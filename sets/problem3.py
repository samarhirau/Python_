n ,m = map (int, input().split())
arr = list (map (int, input().split()))
s1 = set(map(int , input().split() ))
s2 = set(map(int , input().split() ))


happiness = 0

for i in arr:
    if i in s1:
        happiness += 1
    elif i in s2:
        happiness -= 1

print(happiness)

"""
The first line contains integers  and  separated by a space.
The second line contains  integers, the elements of the array.
The third and fourth lines contain  integers,  and , respectively.

Output Format

Output a single integer, your total happiness.
"""