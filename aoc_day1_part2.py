import math

with open('aoc_day1_part1.txt', 'r') as f:
    input = f.read().split('\n')

value = 50
password = 0
for rotation in input:
    direction = rotation[0]
    turn = int(rotation[1:])

    change = 0
    if direction == 'L':
        change = turn - value
        if value != 0:
            change += 100
        value -= turn
    else:
        change = turn + value
        value += turn
    
    password += math.floor(change / 100)
    value %= 100

print('res: ', password)