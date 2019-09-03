# Return True if these two lists have any common element.

lista = [12, 13, 14, 12, 15, 17]
listb = [32, 12, 45, 67, 12, 15]


def get_common_members(la, lb):
    for a in la:
        if a in lb:
            return True
        return False


result = get_common_members(lista, listb)
print(result)
