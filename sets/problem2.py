

size_a = int (input())
a = set (map (int, input().split()))

size_b = int (input())
b = set (map (int, input().split()))

# result = a.symmetric_difference(b)  (A - B) ∪ (B - A)

result = a.difference(b).union(b.difference(a))

for item in sorted (result):
    print (item)