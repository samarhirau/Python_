from collections import Counter

Num_shoes = int(input())
shoes_size_list = list(map(int, input().split()))
Num_customers = int(input())

shoes = Counter(shoes_size_list)
total = 0

for _ in range(Num_customers):
    size, price = map(int, input().split())
    if shoes[size] > 0:
        total += price
        shoes[size] -= 1

print(total)
