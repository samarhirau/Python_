# Equilibrium Index

arr = [1, 3, 5, 2, 2]

for i in range(len(arr)):
    if sum(arr[:i]) == sum(arr[i+1:]):
        print(i)
        break
else:
    print(-1)

    
        
        
        