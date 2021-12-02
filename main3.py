def movements_list():
    with open('D:\list.txt') as file:
        movements = [line.strip() for line in file]
    return movements


def movements_dict():
    movements = {'forward': 0, 'down': 0, 'up': 0}
    for i in movements_list():
        movements[i[:-2]] += int(i[-1])
    return movements


print(movements_dict()['forward'] * (movements_dict()['down'] - movements_dict()['up']))
