n = int(input('Input an integer: '))
for i in range(2, n):
    if i % 5 == 0 or i % 7 == 0:
        print(i)