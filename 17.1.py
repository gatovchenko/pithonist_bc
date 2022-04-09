# 17.7.1
# text = input('Input your text: ')
# vowels = [i for i in text if i in ('у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю')]
# print('Vowels list: ', vowels)
# print('Length of list:', len(vowels))

# 17.7.2
# length = int(input('Input length of list: '))
# list = [(1 if i % 2 == 0 else i % 5) for i in range(length)]
# print(f'Result = {list}.')

# 17.7.3
# import random
#
# team_1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
# team_2 = [round(random.uniform(5, 10), 2) for _ in range(20)]
# print(f'First team: {team_1}.')
# print(f'Second team: {team_2}.')
# result = [team_1[i] if team_1[i] > team_2[i] else team_2[i] for i in range(20)]
# print(f'Result of winners {result}. ')

# 17.7.4
# alphabet = 'abcdefg'
# alphabet_1 = alphabet[:]
# print(alphabet_1)
# print(alphabet[::-1])
# print(alphabet[::2])
# print(alphabet[1::2])
# print(alphabet[:1])
# print(alphabet[len(alphabet):len(alphabet)-2:-1])
# print(alphabet[3:4])
# print(alphabet[len(alphabet)-3: len(alphabet)+1])
# print(alphabet[3:5])
# print(alphabet[4:2:-1])

# 17.7.5
# list = input('Input line:')
# first_h = list.index('h')
# last_h = list.rindex('h')
#
# print(f'Reverse line between h: {list[last_h-1:first_h:-1]}')

# 17.7.6
# import random
#
# number = int(input('Total numbers in list: '))
# start_list = [random.randint(0, 2) for _ in range(number)]
# print(f'Starting list: {start_list}')
# finish_list = [i for i in start_list if i > 0]
# print(f'Finish list: {finish_list}')

# 17.7.7
# list = [[i for i in range(1, 13, 4)], [i for i in range(2, 13, 4)],
#         [i for i in range(3, 13, 4)], [i for i in range(4, 13, 4)]]
# list = [[i, i + 4, i + 8] for i in range(1, 5)]
# print(list)

# 17.7.8
import random

# n = int(input('Number of figures: '))
# k = int(input('Number of throws: '))

# 17.7.9
# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# result = [i for j in nice_list for i_number in j for i in i_number]
# print(result)

#  17.7.10
# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# k = int(input('Input distance k: '))
#
#
# def codding(i):
#     if i not in alphabet:
#         return i
#     else:
#         x = alphabet.index(i)
#         y = alphabet[(x + k) % 33]
#         return y
#
#
# phrase = input('Input phrase: ')
# code = [codding(i) for i in phrase]
# result = ''
# for i in code:
#     result += i
# print(result)
