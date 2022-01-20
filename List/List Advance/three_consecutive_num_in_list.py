# Python program to check if the list contains three consecutive common numbers in Python

List = [4, 5, 5, 5, 3, 8, 8, 8, 9, 9]
# List = [1, 1, 1, 64, 23, 64, 22, 22, 22]

for i in range(0, len(List)-2):
    if List[i] == List[i+1] == List[i+2]:
        print(List[i])
