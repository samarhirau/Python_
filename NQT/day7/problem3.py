# Problem:
# Given a string S, replace every character with the character that comes K places after it in the English alphabet. If it exceeds 'z', it should wrap around to 'a'.

S = "abc"
k = 2


result = ""

for char in S:
    if char.isalpha():
        shifted = (ord(char) - ord('a') + k) % 26 + ord('a')
        result += chr(shifted)
    else:
        result += char
print(result)