# здесь писать код
def summe(x):
    summ = 0
    while x > 0:
        summ += x % 10
        x //= 10
    return summ

def cifre(x):
    count = 0
    while x > 0:
        count += 1
        x //= 10
    return count

number = int(input('Input your number: '))
sum_numbers = summe(number)
cifre_numbers = cifre(number)
difference = abs(sum_numbers - cifre_numbers)
print(f'Sum of cifres = {sum_numbers}.')
print(f'Count of cifres = {cifre_numbers}.')
print(f'Difference sum and count = {difference}.')