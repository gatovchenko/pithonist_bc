word = list(input('Input word: '))
print(word)
unique_letters = 0

for i in word:
    same_letters = 0
    for j in word:
        if i == j:
            same_letters += 1
    if same_letters == 1:
        unique_letters += 1

print(f'Unique letters: {unique_letters}.')
