def movements_list():
    with open('D:\list.txt') as file:
        movements = [line.strip() for line in file]
    return movements


def movements_dict():
    movements = {'forward': 0, 'depths': 0, 'aim': 0}
    for i in movements_list():
        if i[:-2] == 'forward':
            movements['forward'] += int(i[-1])
            movements['depths'] += (movements['aim'] * int(i[-1]))
        elif i[:-2] == 'up':
            movements['aim'] -= int(i[-1])
        elif i[:-2] == 'down':
            movements['aim'] += int(i[-1])
    return movements


print(movements_dict()['forward'] * movements_dict()['depths'])
