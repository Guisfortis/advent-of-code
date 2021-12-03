def make_binary_list():
    with open('D:\list1.txt') as file:
        bits = [line.strip() for line in file]
    return bits


def make_bits_list(number):
    bits_list = []
    for i in range(len(make_binary_list())):
        bits_list += make_binary_list()[i][number]
    return max(bits_list, key=bits_list.count)


def make_gamma_rate():
    gamma_rate = []
    for number in range(len(make_binary_list()[0])):
        gamma_rate += make_bits_list(number)
    return ''.join(gamma_rate)


def make_epsilon_rate():
    epsilon_rate = [str(int(not int(i))) for i in make_gamma_rate()]
    return ''.join(epsilon_rate)


print(int(make_gamma_rate(), base=2) * int(make_epsilon_rate(), base=2))

