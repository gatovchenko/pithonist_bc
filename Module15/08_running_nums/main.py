shift = int(input('Input shift: '))
old_scoreboard = [1, 4, -3, 0, 10]
new_scoreboard = []

count = 0
for i in old_scoreboard:
    count += 1

for i in range(count):
        new_scoreboard.append(old_scoreboard[i - shift])
print(old_scoreboard)
print(new_scoreboard)
