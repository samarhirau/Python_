
# Problem 5: Students in at least one subject
""" There are  students in a college. Some of them have subscribed to the English newspaper,
while some have subscribed to the French newspaper. You are given two sets of roll numbers of students. Your task is to find the total number of students who have subscribed to at least one newspaper.
"""
num_students = int(input())
roll_numbers = set(map(int, input().split()))
num_french = int(input())
sub_french = set(map(int, input().split()))

total = roll_numbers.union(sub_french)
print(len(total))