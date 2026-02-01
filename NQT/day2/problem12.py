# Problem: Check Perfect Number

# A number is perfect if the sum of its proper divisors equals the number itself.


num = int(input())

total = 0
for i in range(1, (num // 2)+1):
    if num % i == 0:
        total += i
if total == num:
    print("Perfect")
    
else:
    print("Not a Perfect")
    
