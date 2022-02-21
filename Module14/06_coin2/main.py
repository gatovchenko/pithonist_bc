# здесь писать код
import math

while True:
    x = float(input('Input coordinate x: '))
    y = float(input('Input coordinate y: '))
    radius = float(input('Input radius of coin: '))
    if math.sqrt(x ** 2 + y ** 2) <= radius:
        print('Coin near!')
    else:
        print('Search again!')
