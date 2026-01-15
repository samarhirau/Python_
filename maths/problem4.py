# problem4.py : Print the series 1, 11, 111, 1111, ... up to n terms


"""
Docstring for maths.problem4
Prints a series where each term consists of repeated '1's up to n terms.

"""

for i in range(1, int(input())+1): print(i * (10**i - 1)//9)
