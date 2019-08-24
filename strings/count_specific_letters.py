# count how many letters are in this sentence except for m
sentence = 'I did like how the kids were dancing'
counter = 0
for a in sentence:
    if a in ('d', ' '):
        continue
    else:
        counter += 1
print(counter)