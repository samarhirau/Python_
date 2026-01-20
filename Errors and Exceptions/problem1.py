# Problem Statement: Print the value of a // b for given integers a and b.
# If b is zero, print "Error Code: integer division or modulo by zero".
# If either a or b is not an integer, print "Error Code: invalid literal for int() with base 10".


T = int(input())
for _ in range(T):
    a, b = input().split()
    try:
        a = int(a)
        b = int(b)
        print(a // b)
    except ZeroDivisionError as zde:
        print("Error Code:", zde)
    except ValueError as ve:
        print("Error Code:", ve)