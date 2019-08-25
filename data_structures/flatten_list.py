# flatten below list
import itertools
lista = [[4, 3], [34, 56, 89], [10, 11], [3, 4]]
result = list(itertools.chain(*lista))
print(result)  # [4, 3, 34, 56, 89, 10, 11, 3, 4]
