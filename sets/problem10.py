# problem10  - find the Captain's Room number
'''
A group of tourists is visiting a country. The tourists are divided into groups of size k, where each group stays in a separate room. However, the captain of the group has a unique room. Given the list of room numbers assigned to each tourist, find the captain's room number.
Input Format:
The first line contains an integer, k, the size of each group.
The second line contains the space-separated room numbers for each tourist.
'''

group_size = int(input())

member_list = list(map(int, input().split()))

unique_rooms = set()
total_sum = 0

for room in member_list:
    total_sum += room
    unique_rooms.add(room)
unique_sum = sum(unique_rooms)

captain_room = (unique_sum * group_size - total_sum) // (group_size - 1)
print(captain_room)

