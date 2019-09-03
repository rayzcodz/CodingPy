# Generate 7 lottery numbers in the range of (0, 9) randomly.
import random
lottery_numbers = []
for n in range(7):
    lottery_numbers.append(random.randint(0, 10))

for number in lottery_numbers:
    print(number)