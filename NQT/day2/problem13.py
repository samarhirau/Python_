# Problem: Check Strong Number

# A number is Strong if the sum of factorials of its digits equals the number.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    return factorial (n - 1) * n

num = input().strip()
total = 0
for ch in num:
    total += factorial(int(ch))
if total == int(num):
    print("Strong")
else:
    print("Not a Strong")


    

