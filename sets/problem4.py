""" Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of  country stamps.

Find the total number of distinct country stamps."""
num_stamp = int(input())

set_list = set()

for i in range(num_stamp):
    set_list.add(input())
    
l = set(set_list)    
print(len(l))