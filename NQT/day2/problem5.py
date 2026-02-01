# Problem: Sum of Prime Numbers in a Range



n, m = map(int, input().split())

total = 0

for num in range(max(2, n), m + 1):
    isPrime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            isPrime = False
            break
    if isPrime:
        total += num

print(total)

        
    
    