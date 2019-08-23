# Write a program to generate numbers in this sequence. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

fibonacci = []

a = 0
b = 1
c = a + b

fibonacci.append(a)
fibonacci.append(b)
fibonacci.append(c)


for i in range(1, 20):
    fibonacci.append(fibonacci[i] + fibonacci[i+1])

print('First {} fibanacci numbers are: {}'.format(len(fibonacci) - 2, fibonacci))
