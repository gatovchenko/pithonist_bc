#
first_list = []
second_list = []

for i in range(160,177,2):
    first_list.append(i)
for i in range(162,181,3):
    first_list.append(i)

first_list.extend(second_list)
first_list.sort()
print(first_list)