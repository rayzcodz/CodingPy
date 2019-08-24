import sys
print(sys.version)


words = 'DC is the capital of the USA'
words_list = words.split(' ')

for i in range(1, len(words_list)+1):
    print(words_list[i * -1], end=' ')

