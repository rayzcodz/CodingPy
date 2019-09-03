# Remove even elements from list

# way 1: solving using for loop
my_list = [23, 21, 22, 4, 5, 6, 78, 98, 65, 43]
evens_a = []
for number in my_list:
    if number % 2 != 0:
        evens_a.append(number)

print(evens_a)

# way 2: solving using list comprehension
evens_b = [number for number in my_list if number % 2 != 0]
print(evens_b)
