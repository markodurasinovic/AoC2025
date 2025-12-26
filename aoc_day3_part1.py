with open('aoc_day3.txt', 'r') as f:
    input = f.read().split('\n')

def find_max(nums, start):
    end = len(nums)
    if(start >= end):
        start = 0
        end -= 1

    max, j = nums[start], start
    for i in range(start, end):
        cur = nums[i]
        if cur > max:
            max, j = cur, i
    return str(max), j

result = 0
for line in input:
    nums = [int(n) for n in line]
    max1, i = find_max(nums, 0)
    max2, j = find_max(nums, i + 1)
    if(i < j):
        result += int(max1 + max2)
    else:
        result += int(max2 + max1)
print(result)