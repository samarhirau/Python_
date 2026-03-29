# Reverse a String Without Using [::-1]

def reverse_str(s):
    stack = list(s)
    res = ""
    while stack:
        res += stack.pop()
    return res

s = "samar"
res = reverse_str(s)
print(res)
        