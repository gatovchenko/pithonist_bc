# здесь писать код
start_year = int(input('Input starting year: '))
finish_year = int(input('Input finish year: '))

for i in range(start_year, finish_year + 1):
    i1 = i % 10
    i2 = (i // 100) % 10
    i3 = (i // 10) % 10
    i4 = i // 1000
    if i1 == i2 == i3 or i1 == i3 == i4 or i2 == i3 == i4:
        print(i)
