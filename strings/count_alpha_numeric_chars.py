# count alpha numeric characters in a string
string = 'asd897sf./*&7878dsf'
counter = 0
for c in string:
    if c.isalnum():
        counter += 1

print(counter)