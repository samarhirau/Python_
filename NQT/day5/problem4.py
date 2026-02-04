
# Problem: "The Character Shift" Given a string and an integer k, shift every character in the string by k positions in the alphabet. If it goes past 'z', it should wrap around to 'a'.

s = "abc"
k = 2
n = len(s)

result = []
for i in range(n):
    ch = s[i]
    shifted_ch = chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
    result.append(shifted_ch)
shifted_string = ''.join(result)
print(shifted_string)