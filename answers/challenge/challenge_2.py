def mathy(l):
    new_list = []
    for i in range(len(l)):
        sum = 0
        for j in range(len(l)):
            sum += (l[i] * l[j])
        new_list.append(sum)
    return new_list

print(mathy([1, 2, 3, 4, 5]))
