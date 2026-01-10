# Print the average marks of the list corrected to 2 decimal places.
from collections import namedtuple

n = int(input())
columns = input().split()
Student = namedtuple('Student', columns)

total = 0
for _ in range(n):
    s = Student(*input().split())
    total += int(s.MARKS)

print(f"{total/n:.2f}")
