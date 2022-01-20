# Python program to interchange first and last elements in a list

List = [2, 3, 4, 9, 7, 6, 8]
print(List)

# Interchange first and last Element
List[0], List[-1] = List[-1], List[0]
print(List)