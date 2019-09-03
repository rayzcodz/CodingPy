# Insert a given string at the beginning of all items in a list.

list_a = [1, 2, 3, 4]
list_b = []

for n in list_a:
    m = 'abc' + str(n)
    list_b.append(m)

print(list_b)


#  way 2 list comprehension
list_c = ['abc{}'.format(i) for i in list_a]
print(list_c)
