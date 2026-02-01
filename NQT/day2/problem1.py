# Problem: Check Palindrome String

s = input().strip()

isPalindrome = True

for i in range(len(s)//2):
    if s[i] != s[len(s)-1-i]:
        isPalindrome = False
        break

if isPalindrome:
    print("Palindrome")
else:
    print("Not Palindrome")
