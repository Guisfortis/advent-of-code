with open('D:\list.txt') as file:
    depths = [int(line.strip()) for line in file]
count = 0
print(depths)
for i in range(3, len(depths)):
    if sum(depths[i - 2: i + 1]) > sum(depths[i - 3: i]):
        count += 1
print(count)
