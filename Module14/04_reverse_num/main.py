# здесь писать код
def conversly(x):
    start_number, finish_number = '', ''
    stop = 0
    for i in x:
        if i != '.' and stop == 0:
            start_number = i + start_number
        elif i == '.':
            stop += 1
        else:
            finish_number = i + finish_number
    finish = start_number + '.' + finish_number
    return float(finish)


first_num = input('Input your first number: ')
second_num = input('Input your first number: ')

converse_num1 = conversly(first_num)
converse_num2 = conversly(second_num)
summ = converse_num1 + converse_num2
print(f'First converse number = {converse_num1}.')
print(f'Second converse number = {converse_num2}.')
print(f'Sum of converse numbers = {summ}.')
