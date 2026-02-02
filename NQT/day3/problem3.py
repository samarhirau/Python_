# Question 4: Longest Word in a Sentence

s = "TCS is a very good company"

words = s.split()

longest_word = ''
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word)




    
    