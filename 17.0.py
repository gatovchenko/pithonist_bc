# 17.2.1
# a = int(input('Input start number A: '))
# b = int(input('Input finish number B: '))
#
# square_ab = [x ** 2 for x in range(a, b + 1)]
# cube_ab = [x ** 3 for x in range(a, b + 1)]
# print(f'List squares number at {a} to {b}: {square_ab}.')
# print(f'List cubes number at {a} to {b}: {cube_ab}.')


# 17.2.2
# list_words = []
# word = input('Input word: ')
# symbol = input('Input symbol: ')
# list_words.extend(word)
# list_words_double = [x+x for x in list_words]
# list_words_sym = [x+x+symbol for x in list_words]
# print(f'List of double symbols: {list_words_double}.')
# print(f'List of double symbols + sym: {list_words_sym}.')

# 17.2.3
# def prices(x, increase):
#     return round((x * (1 + increase / 100)), 2)
#
#
# list_prices = []
# for i in range(5):
#     price = float(input(f'Products price {i + 1}:'))
#     list_prices.append(price)
# print(list_prices)
#
# first_price_increase = int(input('Input price increase of first year: '))
# second_price_increase = int(input('Input price increase of second year: '))
#
# first_year_prices = [prices(x, first_price_increase) for x in list_prices]
# second_year_prices = [prices(x, second_price_increase) for x in first_year_prices]
#
#
# print(first_year_prices)
# print(second_year_prices)
# print('Total summ of years:', round(sum(list_prices), 2), round(sum(first_year_prices), 2), round(sum(second_year_prices), 2))

# 17.3.1
# a = int(input('Input started number: '))
# b = int(input('Input finish number: '))
# list_even = [x for x in range(a, b + 1) if x % 2 == 0]
# print('List even numbers: ', list_even, '.')

# 17.3.2
# original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# new_prices = [i_price if i_price >= 0 else 0 for i_price in original_prices]
# print('New prices: ', new_prices)

# 17.3.3
# import random
#
# squad_1 = [random.randint(50, 80) for _ in range(10)]
# squad_2 = [random.randint(30, 60) for _ in range(10)]
# squad_3 = [('Погиб' if (squad_1[i_monster] + squad_2[i_monster] > 100) else 'Выжил') for i_monster in range(10)]
#
# print('Damage first squad: ', squad_1)
# print('Damage second squad: ', squad_2)
# print('Condition of third squad: ', squad_3)

# 17.4.1
# original_prices = [-12, 3, 5, -2, 1]
# new_prices = [0 if original_prices[i_price] < 0 else original_prices[i_price]
#               for i_price in range(len(original_prices))]
# print("Мы потеряли: ",  abs(sum(original_prices) - sum(new_prices)))

# 17.4.2
# nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
# print(nums[:5])
# print(nums[:len(nums)-2])
# print(nums[:8])
# print(nums[::2])
# print(nums[1::2])
# print(nums[::-1])
# print(nums[::-2])

# 17.4.3
# import random
#
# a = random.randint(0, 8)
# b = random.randint(a + 1, 9)
# list = [random.randint(10, 30) for _ in range(10)]
# print(list)
# list[a:b + 1] = []
# print(list)
# print(a, b)
