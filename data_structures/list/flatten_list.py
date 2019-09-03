# flatten below list
import itertools
list_a = [[4, 3], [34, 56, 89], [10, 11], [3, 4]]
result = list(itertools.chain(*list_a))
print(result)  # [4, 3, 34, 56, 89, 10, 11, 3, 4]
