def find_second_occurrence(l, target):
    first = False
    for i in range(len(l)):
        if l[i] == target:
            if not first:
                first = True
            else:
                return i
    return -1

print(find_second_occurrence([1, 2, 3, 4, 4, 5, 6, 7, 4], 4))
print(find_second_occurrence([1, 2, 3, 4, 4, 5, 6, 7, 4], 2))