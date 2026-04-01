# Check if a String is a Palindrome
# Write a Python function called is_palindrome that takes a string and returns True if it is a palindrome, otherwise False.


def is_palindrome(s):
    filtered = ""
    
    for ch in s:
        if ch.isalpha():
            filtered += ch.lower()
    
    j = 0
    for i in range(len(filtered)-1, -1, -1):
        if filtered[i] != filtered[j]:
            return False
        j += 1
        
    return True

s = "A man, a plan! a canal Panama"
print(is_palindrome(s))