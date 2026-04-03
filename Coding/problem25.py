# Group Anagrams Together
# Write a Python function called group_anagrams that takes a list of strings and groups the anagrams together.




def group_anagrams(arr):
    if not arr:
        return []
    
    groups = {}  # key=sorted word, value=list of anagrams
    
    for word in arr:
        key = "".join(sorted(word))  # "eat" → "aet" ✅
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    
    return list(groups.values())

arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(arr))

