# Create two dim list and fill it with user entry.

# Creating the two dim list and giving zeros as initial values.
two_dim_list = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for r in range(5):
    for c in range(3):
        two_dim_list[r][c] = input('Enter a numbe: ')
print(two_dim_list)

print(two_dim_list[1][2])
