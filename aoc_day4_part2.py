with open('aoc_day4.txt', 'r') as f:
    input = f.read().split('\n')

grid = [[line[i] for i in range(len(line))] for line in input]
N = len(grid)
M = len(grid[0])


def check_bounds(i, j):
    return i >= 0 and i < N and j >= 0 and j < M

def handle_removal(i, j, counts, grid, rolls):
    grid[i][j] = 'x'
    rolls += 1

    for ii in range(i - 1, i + 2):
        for jj in range(j - 1, j + 2):
            if ii == i and jj == j:
                continue

            if check_bounds(ii, jj):
                if grid[ii][jj] != '@':
                    continue

                counts[ii][jj] -= 1
                if counts[ii][jj] < 4:
                    rolls = handle_removal(ii, jj, counts, grid, rolls)

    return rolls

def solve():
    rolls = 0

    counts = [[0 for j in range(M)] for i in range(N)]
    for i in range(N):
        for j in range(M):
            if grid[i][j] == '@':
                for ii in range(i - 1, i + 2):
                    for jj in range(j - 1, j + 2):
                        if ii == i and jj == j:
                            continue

                        if check_bounds(ii, jj) and grid[ii][jj] == '@':
                            counts[ii][jj] += 1

    for i in range(N):
        for j in range(M):
            if grid[i][j] == '@' and counts[i][j] < 4:
                rolls = handle_removal(i, j, counts, grid, rolls)

    return rolls

print(solve())