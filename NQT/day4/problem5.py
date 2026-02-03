# Harshad Number

num = input().strip()

total = 0
for ch in num:
    total += int(ch)

if int(num) % total == 0:
    print("Harshad")
else:
    print("Not Harshad")





