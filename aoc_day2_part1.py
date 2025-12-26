with open('aoc_day2.txt', 'r') as f:
    input = f.read().split(',')

def is_invalid(id):
    L = len(id)
    chunksize = L//2
    if(id[:chunksize] == id[chunksize:]):
        return True

    return False

invalid_ids = []
for line in input:
    [start, end] = line.split('-')
    while(int(start) <= int(end)):
        if(is_invalid(start)):
            invalid_ids.append(int(start))
        start = str(int(start) + 1)

print(sum(invalid_ids))
