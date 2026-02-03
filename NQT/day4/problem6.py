# Longest Palindromic Substring

s = "babad"


n = len(s)
max_len = 1
start = 0

for i in range(n):
    # Odd length palindromes
    l, r = i, i
    while l >= 0 and r < n and s[l] == s[r]:
        if (r - l + 1) > max_len:
            max_len = r - l + 1
            start = l
        l -= 1
        r += 1

    # Even length palindromes
    l, r = i, i + 1
    while l >= 0 and r < n and s[l] == s[r]:
        if (r - l + 1) > max_len:
            max_len = r - l + 1
            start = l
        l -= 1
        r += 1
print(s[start:start + max_len])
