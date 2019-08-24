# WAP that sorts list of string by their length
a = 'american'
b = 'anna'
c = 'mamana'
d = 'dondurma'
e = 'reads'
f = 'ana'

word_list = []

word_list.append(a)
word_list.append(b)
word_list.append(c)
word_list.append(d)
word_list.append(e)
word_list.append(f)


# creating custom function that will sort our list by len of the elements
def sort_by_len(val):
    return len(val)


print(word_list)

# calling our function
word_list.sort(key=sort_by_len)

print(word_list)



