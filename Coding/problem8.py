# Check if Two Strings are Anagrams
# Write a Python function called is_anagram that takes two strings as input and returns True if they are anagrams of each other, otherwise False.
# dont use sorted function

def is_anagram(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    
    if len(s1) != len(s2):
        return False
    
    char_count = {}
    
    for char in s1:
        char_count[char] = char_count.get(char, 0) + 1
        
    for char in s2:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1
        
    return True
    

string1 = "listen"
string2 = "silent"
result = is_anagram(string1, string2)
print(result)