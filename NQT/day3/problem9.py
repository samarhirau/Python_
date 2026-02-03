# Question 9: Longest Common Prefix

s = "flower flow flight"

words = s.split()

prefix = words[0]

for word in words[1:]:
    while word[:len(prefix)] != prefix and prefix:
        prefix = prefix[:-1]

if prefix:
    print(prefix)
else:
    print(-1)
