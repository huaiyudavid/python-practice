n = int(input('Input an integer: '))
for width in range(1, n+1):
    for i in range(width):
        print('*', end='')
    print('') # For a newline
    