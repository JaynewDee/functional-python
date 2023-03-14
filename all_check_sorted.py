list1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
list2 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def is_sorted(list):
    return all(list[i] <= list[i + 1] for i in range(len(list) - 1))


print(is_sorted(list1))
print(is_sorted(list2))
