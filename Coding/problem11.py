# Count Vowels and Consonants in a String
# Write a Python function called count_vowels_consonants that takes a string and returns a dictionary with count of vowels and consonants.

def count_vowels_consonants(s):
    vowels = 0
    consonants = 0
    for ch in s:
        if ch in "aieouAEIOU":
            vowels += 1
        elif ch.isalpha():
            consonants += 1
    return {'vowels': vowels, 'consonants': consonants}

s = "aeiou"

print(count_vowels_consonants(s))



            
    