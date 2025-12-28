with open('aoc_day5.txt', 'r') as f:
    ranges, ids  = f.read().split('\n\n')

def can_combine(curr, next):
    return curr[0] <= next[0] and curr[1] >= next[0]

def combine(curr, next):
    return [curr[0], max(curr[1], next[1])]

sorted_ranges = ranges.split('\n')
sorted_ranges = [r.split('-') for r in sorted_ranges]
sorted_ranges = [[int(r[0]), int(r[1])] for r in sorted_ranges]
sorted_ranges.sort()

combined_ranges = []
i = 0
curr = None
while i < len(sorted_ranges):
    if curr is None:
        curr = sorted_ranges[i]

    if can_combine(curr, sorted_ranges[i]):
        curr = combine(curr, sorted_ranges[i])
        i += 1
    else:
        combined_ranges.append(curr)
        curr = None
if curr is not None:
    combined_ranges.append(curr)

def is_fresh(id):
    for r in combined_ranges:
        if id >= r[0] and id <= r[1]:
            return True
        if id < r[0]:
            return False
    return False

# part1
fresh_count = 0
for id in ids.split('\n'):
    if is_fresh(int(id)):
        fresh_count += 1
print(fresh_count)

# part2
max_possible_fresh_count = 0
for r in combined_ranges:
    max_possible_fresh_count += r[1] - r[0] + 1
print(max_possible_fresh_count)