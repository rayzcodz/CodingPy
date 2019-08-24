# count how many d is in this statement
sentence = 'The quick brown fox jumps over the lazy dog.'  # this sentence has all 26 chars

# way 1: for loop
letter = 'd'
counter1 = 0
for i in range(len(sentence)):
    if sentence[i] == letter:
        counter1 += 1
print(counter1)

# way 2: for each loop
counter2 = 0
for x in sentence:
    if x == letter:
        counter2 += 1
print(counter2)

#
counter3 = 0
for x in sentence:
    if x == letter:
        counter3 += 1
print(counter3)