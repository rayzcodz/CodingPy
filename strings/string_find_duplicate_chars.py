# You need to write a program in Java to print duplicate characters from a given String.
name = 'Bararck Obamam'
name_list = []
duplicate_chars = []

for a in name:
    if a not in name_list:
        name_list.append(a)
    else:
        duplicate_chars.append(a)
print('Duplicate chars in {} are {}'.format(name, duplicate_chars))

for a in duplicate_chars:
    print('{} repeats {} times'.format(a, duplicate_chars.count(a) + 1))
    