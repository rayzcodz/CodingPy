# Iterate over two lists.
list_a = ['a', 'b', 'c', 'd']
list_b = [1, 2, 3, 4]
list_c = [100, 200, 300, 400]

for x, y in zip(list_a, list_b):
    print(x, y)


# optional additional practice
for x, y in zip(zip(list_a, list_b), list_c):
    print(x, y)

print(list_c.extend(list_b))

