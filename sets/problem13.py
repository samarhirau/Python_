#  Problem 13: Print the sum of the elements of set  on a single line.



set_size = int(input()) 
setA = set(map(int, input().split()))
num_commands = int(input())

for _ in range(num_commands):
    command_line = input().split()
    command = command_line[0]

    if command in ("remove", "discard"):
        element = int(command_line[1])
        if command == "remove" and element in setA:
            setA.remove(element)
        else:
            setA.discard(element)
    elif command == "pop":
        if setA:
            setA.remove(min(setA))  # remove smallest element for consistent output

print(sum(setA))




"""
s = {1,2,3,4,5}
print(s.pop())  # Might print 1, or 2, or any element
print(s)        # Remaining elements, unpredictable order
set.pop() does exist, and it removes an element, but it doesn’t remove the “first” or “smallest” element.

It removes an arbitrary element — basically whatever Python’s set decides internally.

That’s why, in your input, calling pop() multiple times can give different final sums (6 in your run, 4 in another), because sets are unordered.
"""