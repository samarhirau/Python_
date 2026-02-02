# Question 6: Count Frequency of Each Word

s = "TCS is good TCS is best"

freq = {}

words = s.split()

for word in words:
    if not word in freq:
        freq[word] = 1
    else:
        freq[word] +=1


for word in freq:
    print(word, freq[word])

        