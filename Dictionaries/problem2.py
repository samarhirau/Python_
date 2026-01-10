# defaultdict usage to group indices of words from Group A and query them with words from Group B

from collections import defaultdict

n, m = map(int, input().split())

d = defaultdict(list)

# Group A
for i in range(1, n + 1):
    word = input().strip()
    d[word].append(i)

# Group B
for _ in range(m):
    word = input().strip()
    if word in d:
        print(*d[word])  #    * list ko space-separated print karta hai
    else:
        print(-1)
