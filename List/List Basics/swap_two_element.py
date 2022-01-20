# Python program to swap two elements in a list

List = [10, 20, 30, 40, 50]
print(List)
pos1, pos2 = 2, 5

# Because list index start with 0
pos1, pos2 = pos1-1, pos2-1

List[pos1], List[pos2] = List[pos2], List[pos1]

# After Swap
print(List)