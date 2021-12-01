with open('D:\list.txt') as file:
    count = 0
    depths = [line.strip() for line in file]
    for i in range(3, len(depths)):
        if sum([int(depths[i]), int(depths[i - 1]), int(depths[i - 2])]) > sum([int(depths[i - 1]), int(depths[i - 2]), int(depths[i - 3])]):
            count += 1
print(count)
