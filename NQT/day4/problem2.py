# Reverse each word in a sentence

s = "TCS Coding Test"

arr = s.split()
reverse = []

for word in arr:
    reverse.append(word[::-1])
    
print(' '.join(reverse))