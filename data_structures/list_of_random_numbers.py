# generate a list of random numbers 1-100

import random

my_list = []

for n in range(100):
    my_list.append(random.randint(1, 101))

print(my_list)
