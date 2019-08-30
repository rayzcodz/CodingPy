# Write a Python program to get a string made of the first 2 and the last 2
# chars from a given a string. If the string length is less than 2,
# return the str.

string = ['', 'anador', 'as', 'soba']


def first2last2(some_string):
    if len(some_string) <= 2:
        return some_string
    else:
        result = some_string[0:2] + some_string[-2:]
        return result


for word in string:
    print(first2last2(word))


