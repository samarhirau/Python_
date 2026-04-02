# Capitalize First Letter of Each Word Without Using .title()
# Write a Python function called capitalize_words that takes a string and returns the string with the first letter of each word capitalized.
def capitalize_words(s):
    if not s:
        return ""
    
    words = s.split()
    
    for i in range(len(words)):
        first = words[i][0]
        if 'a' <= first <= 'z':  
            words[i] = chr(ord(first) - 32) + words[i][1:]
    
    return ' '.join(words)

input_string = "hello world from python"
print(capitalize_words(input_string))  




