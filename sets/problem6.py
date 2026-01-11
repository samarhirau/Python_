# Problem Statement: Given two sets of student roll numbers, one for students enrolled in a Mathematics course and another for students enrolled in an English course, find the number of students who are enrolled in both courses.
""" There are  students in a college. Some of them are enrolled in a Mathematics course,
while some are enrolled in an English course. You are given two sets of roll numbers of students. Your task is to find the total number of students who are enrolled in both courses.
"""

sub_english = int(input())
roll_students1 = set(map(int, input().split()))
num_french = int(input())
roll_students2 = set(map(int, input().split()))

print(len(roll_students1.intersection(roll_students2)))