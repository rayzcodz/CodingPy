# Insert a char before each element in a list
# Original List:  ['Red', 'Green', 'Black']
# Original List:  ['c', 'Red', 'c', 'Green', 'c', 'Black']

list_a = ['Red', 'Green', 'Black']

i = 1

while i <= 6:
    list_a.insert(-i, 'c')
    i = i + 2
print(list_a)  # ['c','Red', 'c','Green', 'Black']


