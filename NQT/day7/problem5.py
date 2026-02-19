# Problem: "Rearrange by Frequency"
# Given a string, sort it based on the frequency of characters in descending order. If two characters have the same frequency, sort them alphabeticallS

S = "banana"

def frequency_sort(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    char_list = list(s)
    
    char_list.sort(key=lambda x: (-freq[x], x))
    
    return "".join(char_list)

print(frequency_sort("banana")) 
print(frequency_sort("tree"))   