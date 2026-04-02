# Count Words in a String Without Using .split()
# Write a Python function called count_words that takes a string and returns the total number of words in it without using .split()

def count_words(s):
    if len(s) == 0:
        return 0
    
    count = 0
    in_word = False
    for char in s:
        if char != ' ' and not in_word:
            count += 1
            in_word = True
        elif char == ' ':
            in_word = False
    return count


s = "oneword"
print(count_words(s))
