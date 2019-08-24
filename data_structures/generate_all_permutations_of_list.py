# WAP Python program to generate all permutations of a list in Python.
import itertools
list_a = [2, 4, 5, 6]
# list_a = ['a', 'b', 'c', 'd']

result = list(itertools.permutations(list_a))
print(result)
