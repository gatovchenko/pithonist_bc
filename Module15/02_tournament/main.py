name_list = ['Artem', 'Boris', 'Vlad', 'Gosha', 'Dima', 'Eugenii', 'Jhenya', 'Zahar']
first_day_list = []
count = 0
for i in name_list:
    if count % 2 == 0:
        first_day_list.append(i)
    count += 1
print(f'First day list: {first_day_list}.')
