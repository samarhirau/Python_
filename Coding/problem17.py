# Find the Longest Word in a String
# Write a Python function called longest_word that takes a string and returns the longest word in it.

def longest_word(s):
    if not s:
        return ""
    
    words = s.split()
    longest = ""
    max_len = 0
    
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
            longest = word
    
    return longest

s = "I love programming in Python"
print(longest_word(s))  