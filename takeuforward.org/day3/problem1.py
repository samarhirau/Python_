# Check if the given String is Palindrome or not

inputString = input("Enter a string: ")

reversed_str = inputString[::-1]
poli = True

for i in range(len(inputString)):
    if inputString[i] != reversed_str[i]:
        poli = False
        break

print(poli)

    