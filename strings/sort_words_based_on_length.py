# WAP that sorts list of string by their length
a = 'american'
b = 'anna'
c = 'mamana'
d = 'dondurma'
e = 'reads'
f = 'ana'


word_list = []  # ['american', 'anna', 'mamana', 'dondurma', 'reads', 'ana']


word_list.append(a)
word_list.append(b)
word_list.append(c)
word_list.append(d)
word_list.append(e)
word_list.append(f)


# way 1
# creating custom function that will sort our list by len of the elements
def sort_by_len(val):
    return len(val)


print(word_list)

# calling our function
word_list.sort(key=sort_by_len)

print(word_list)


# way 2
word_dict = {}
word_dict.update(american=len('american'))
word_dict.update(anna=len('anna'))
word_dict.update(mamana=len('mamana'))
word_dict.update(dondurma=len('dondurma'))
word_dict.update(read=len('read'))
word_dict.update(ana=len('ana'))

print(word_dict)
sorted_word_dict = sorted(word_dict.items(), key=lambda kv: kv[1])

for x in sorted_word_dict:
    print(x[0])