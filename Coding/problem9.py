# Find the Longest Common Prefix
# Write a Python function called longest_common_prefix that takes a list of strings and returns the longest common prefix among all strings.

def longest_common_prefix(arr):
    pre = ""
    for ch in arr:
        if pre == "":
            pre = ch
        else:
            while not ch.startswith(pre):
                pre = pre[:-1]
                if pre == "":
                    return ""
                
        
    return pre

# Example usage:
strings = ["flower", "flow", "flight"]
result = longest_common_prefix(strings)
print(result)  
        

    