word = list(input('Input word: '))
print(word)
count = 0
for i in word:
    count += 1

part_word1, part_word2 = '', ''
for i in range(count):
    if i < count // 2:
        part_word1 += word[i]
    elif i >= count - i:
        part_word2 = word[i] + part_word2

print(part_word1)
print(part_word2)

if part_word1 == part_word2:
    print('Pallindrom!')
else:
    print('Its not a pallindrom!')