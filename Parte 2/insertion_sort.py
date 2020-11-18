def insertion_sort(list: list) -> list:
    list = list[:]
    for i in range(len(list)):
        for j in range(i, 0, -1):
            if list[j] < list[j-1]:
                list[j], list[j-1] = list[j-1], list[j]
    return list
