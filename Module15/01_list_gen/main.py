n = int(input('Input number: '))
odd_numberlist = []
for i in range(n+1):
    if i % 2 != 0:
        odd_numberlist.append(i)
print(f'Odd number list to {n}: {odd_numberlist}.')
