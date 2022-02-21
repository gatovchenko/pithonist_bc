# здесь писать код
def nok(x):
    least = 0
    for i in range((x + 1), 1, -1):
        if x % i == 0:
            least = i
    return least

while True:
    number = int(input('Input your number: '))
    least_nok = nok(number)
    print(f'Least nok of {number} = {least_nok}.')
    print()