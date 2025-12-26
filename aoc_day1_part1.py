with open('aoc_day1.txt', 'r') as f:
    input = f.read().split('\n')

value = 50
password = 0
for rotation in input:
    if(value == 0):
        password += 1
    direction = rotation[0]
    turn = int(rotation[1:]) % 100
    value += (turn if direction == 'L' else -turn)
    if(value > 99):
        value = value % 100
    elif(value < 0):
        value = 100 + value

print(password)