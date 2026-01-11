# You are given a complex z. Your task is to convert it to polar coordinates.

import cmath


z = complex(input())
print(abs(z))
print(cmath.phase(z))