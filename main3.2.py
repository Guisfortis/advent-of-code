def make_binary_list():
    with open('D:\list1.txt') as file:
        bits = [line.strip() for line in file]
    return bits


def find_max_count(new_list, number):
    count_1 = 0
    count_0 = 0
    for i in new_list:
        if i[number] == '1':
            count_1 += 1
        else:
            count_0 += 1
    if count_1 >= count_0:
        first_number = '1'
    else:
        first_number = '0'
    return first_number


def find_min_count(new_list, number):
    count_1 = 0
    count_0 = 0
    for i in new_list:
        if i[number] == '1':
            count_1 += 1
        else:
            count_0 += 1
    if count_0 <= count_1:
        first_number = '0'
    else:
        first_number = '1'
    return first_number


def make_oxygen_generator_rating(new_list, number):
    first_number = find_max_count(new_list, number)
    for i in new_list[::-1]:
        if i[number] != first_number:
            new_list.remove(i)
    number += 1
    if len(new_list) != 1:
        return make_oxygen_generator_rating(new_list, number)
    return new_list[0]


def make_c02_scrubber_rating(new_list, number):
    first_number = find_min_count(new_list, number)
    for i in new_list[::-1]:
        if i[number] != first_number:
            new_list.remove(i)
    number += 1
    if len(new_list) != 1:
        return make_c02_scrubber_rating(new_list, number)
    return new_list[0]


print(int(make_oxygen_generator_rating(make_binary_list(), 0), base=2) * int(make_c02_scrubber_rating(make_binary_list(), 0), base=2))
