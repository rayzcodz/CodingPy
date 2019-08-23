# using string slice
name = 'Fernando'
reversed_name1 = name[len(name)::-1]
print(reversed_name1)


# using for loop
reversed_name2 = ''
for i in range(1, len(name)+1):
    reversed_name2 += name[i*-1]
print(reversed_name2)


# using while loop
reversed_name3 = ''
i = 1
while i < len(name) + 1:
    reversed_name3 += name[i*-1]
    i += 1
print(reversed_name3)
