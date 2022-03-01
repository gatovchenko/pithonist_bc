total_boxes = int(input('Total boxes: '))
boxes = []
for i in range(total_boxes):
    weight_box = int(input(f'Weight of {i+1} box: '))
    if weight_box > 200:
        print(f'Weight > 200. Correction: weight {i+1} box = 200.')
        weight_box = 200
    boxes.append(weight_box)

print(boxes)
last_box = int(input('Weight of last box: '))
count = 1
for i in boxes:
    if i >= last_box:
        count += 1
    else:
        break
print(f'Number of last box = {count}.')
