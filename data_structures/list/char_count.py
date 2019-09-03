# WAP to find how many times each char repeats in a sentence.

string = 'Madacascar'
char_count = {}

for c in string:
    if c not in char_count:
        char_count[c] = 1
    else:
        char_count[c] = char_count.get(c) + 1

print(char_count)
