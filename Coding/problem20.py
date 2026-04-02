# Generate All Substrings of a String
# Write a Python function called all_substrings that takes a string and returns all possible substrings of it.

def all_substrings(s):
    substrings = []
    n = len(s)
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.append(s[i:j])
    
    return substrings

input_string = "abc"
print(all_substrings(input_string))