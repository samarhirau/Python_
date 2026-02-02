
# Question 5: Remove All Duplicate Characters (Keep First Occurrence)

s = "programming"

seen = ''
for ch in s:
    if ch not in seen:
        seen += ch

print(seen)
