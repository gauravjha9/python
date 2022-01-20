# Python | Remove empty tuples from a list

List = [(), ('ram', '15', '8'), (), ('laxman', 'sita'),
        ('krishna', 'akbar', '45'), ('', ''), ()]
print(List)

List = [t for t in List if t]
print('After remove empty tuple: ',List)
