number = int(input('Input total cards: '))
old_cardlist = []
new_cardlist = []
for i in range(number):
    card = int(input(f'{i+1} Videocard: '))
    old_cardlist.append(card)
print(f'Old cardlist: {old_cardlist}.')
maxnum = old_cardlist[0]
for i in old_cardlist:
    if i > maxnum:
        maxnum = i
for i in old_cardlist:
    if i != maxnum:
        new_cardlist.append(i)
print(f'New cardlist: {new_cardlist}.')
