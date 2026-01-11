# Problem 8: Find the total number of students who are enrolled in either English or French but not both.
""" There are  students in a college. Some of them are enrolled in an English course,
while some are enrolled in a French course. You are given two sets of roll numbers of students. Your task is to find the total number of students who are enrolled in either English or French but not both.
"""

sub_english = int(input())
roll_english = set(map(int, input().split()))
num_french = int(input())
roll_french = set(map(int, input().split()))

print(len(roll_english.symmetric_difference(roll_french)))