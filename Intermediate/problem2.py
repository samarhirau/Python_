# Find All Permutations of a String
# Write a Python function called permutations that takes a string and returns all possible permutations of it.

def permutations(s):
    if not s:          
        return []
    if len(s) == 1:     
        return [s]
    
    perm_list = []
    
    for i, char in enumerate(s):
        remaining = s[:i] + s[i+1:]
        for perm in permutations(remaining):
            perm_list.append(char + perm)
    
    return perm_list

print(permutations("abc"))