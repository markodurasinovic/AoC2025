with open('aoc_day4.txt', 'r') as f:
    input = f.read().split('\n')

grid = [[line[i] for i in range(len(line))] for line in input]
rolls = 0
N = len(grid)
M = len(grid[0])
for i in range(N):
    for j in range(M):
        if grid[i][j] == '.':
            continue
        neighbours = 0
        for ii in range(i - 1, i + 2):
            for jj in range(j - 1, j + 2):
                if ii == i and jj == j:
                    continue
                if ii >= 0 and ii < N and jj >= 0 and jj < M:
                    if grid[ii][jj] == '@':
                        neighbours += 1
        if neighbours < 4:
            rolls += 1
print(rolls)