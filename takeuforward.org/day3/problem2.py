# Count number of vowels, consonants, spaces in String


rawstr ="Take u forward is Awesome"

vowels = 0
consonants = 0
spaces = 0

for char in rawstr:
    if char in 'aeiouAEIOU':
        vowels += 1
    elif char == ' ':
        spaces += 1
    else:
        consonants += 1
        
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Spaces:", spaces)