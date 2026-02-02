# Problem: Sum of Numbers in a String
s = "12abc20yz68"

new = ''

for ch in s:
    if not ch.isdigit():
        new += ' '
    else:
        new += ch
num_list = new.split()
total = 0
for num in num_list:
    total += int(num)
print(total)