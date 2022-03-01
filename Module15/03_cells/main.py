number = int(input('Input total numbers: '))
count = 1
ceils_uncorrect = []
for i in range(number):
    efficiency = int(input(f'Input efficiency of ceil # {i+1}: '))
    if count > efficiency:
        ceils_uncorrect.append(efficiency)
    count += 1
# print(f'Uncorrect ceils: {ceils_uncorrect}')
print('Uncorrect ceils:', end = ' ')
for i in ceils_uncorrect:
    print(i, end = ' ')
