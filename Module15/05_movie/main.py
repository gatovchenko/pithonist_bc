films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
films_list = []
number = int(input('How many films do you want add for your list: '))
for i in range(number):
    film_chek = input('Input name film: ')
    for i in films:
        if i == film_chek :
            films_list.append(film_chek)
            break
    else:
        print(f'We have not {film_chek}.')
print('You favorite films list: ', end = '')
for i in films_list:
    print(i, end = ' ')
