# Adding Element in an Array

N = int(input())
arr = list(map(int, input().split()))

for _ in arr:
    opration = input().split()
    num = opration[1]

    if (opration[0] == 'insertbeginning'):
        arr.insert(0, int(num))
    if (opration[0] == 'insertending'):
        arr.append(int(num))
        
    if (opration[0] == 'insertatpos'):
        arr.insert(int(opration[1]), int(opration[2]))
        
    
print(arr)