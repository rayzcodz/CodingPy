# find out if two lists are circularly identical
list_a = [10, 10, 0, 0, 10]
list_b = [10, 10, 10, 0, 0]

circular = False

if len(list_a) == len(list_b):
    for a in list_a:
        if a in list_b and list_a.count(a) == list_b.count(a):
            circular = True
        else:
            circular = False
            break
else:
    circular = False

print(circular)