# Write a Python program to count the number of strings where the string length is 2 or
# more and the first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

my_list = ['abc', 'xyz', 'aba', '1221']
counter = 0

for elem in my_list:
    if len(elem) > 2 and elem[0] == elem[-1]:
        counter += 1
print(counter)