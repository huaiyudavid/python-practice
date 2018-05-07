age = float(input('Input dog age in human years: '))
dog_age = 0
for i in range(1, age+1):
    if i <= 2:
        dog_age += 10.5
    else:
        dog_age += 4
print(dog_age)