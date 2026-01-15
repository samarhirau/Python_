# Problem 11: Output True or False for each test case on separate line

'''
You are given two sets, A and B. Your job is to find whether set A is a subset of set B.
Input Format:
The first line contains the number of test cases, T.
The first line of each test case contains the number of elements in set A.
The second line of each test case contains the space-separated elements of set A.
The third line of each test case contains the number of elements in set B.
The fourth line of each test case contains the space-separated elements of set B.
'''
test_cases = int(input())
for _ in range(test_cases):
    n_a = int(input())
    set_a = set(map(int, input().split()))
    n_b = int(input())
    set_b = set(map(int, input().split()))
    
    if set_a.issubset(set_b):
        print("True")
    else:
        print("False")

        