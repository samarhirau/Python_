# (Explanation: 1³ + 5³ + 3³ = 153)

# Problem: Check Armstrong Number


num = input().strip()
n = len(num)

total = 0
for ch in num:
    total += int(ch) ** n

if total == int(num):
    print("Armstrong")
else:
    print("Not an Armstrong")

