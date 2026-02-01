# Problem: Replace Vowels with *


s = input().strip()
new = ""

for ch in s:
    if ch.lower() in "aeiou":
        new += "*"
    else:
        new += ch

print(new)
