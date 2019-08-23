# check if below string is a palindrome

city = 'cccco'

# way 1: this code is good but we end up comparing letters more than we need
for i in range(0, len(city)):
    if city[i] != city[(i+1) * -1]:
        is_palindrome1 = 'No'
        break
print(is_palindrome1)


# way 2: this code is longer but it is faster
stopper = ''
is_palindrome2 = 'Yes'
if len(city) // 2 == 0:
    stopper = len(city) // 2 - 1
else:
    stopper = len(city) // 2

for i in range(0, stopper):
    if city[i] != city[(i+1) * -1]:
        is_palindrome2 = 'No'
        break
print(is_palindrome2)
