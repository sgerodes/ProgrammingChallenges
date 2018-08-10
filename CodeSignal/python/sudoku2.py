def sudoku2(grid):
    for line in grid:
        if not valid_subset(line):
            return False
    for column in list(zip(*grid)):
        if not valid_subset(column):
            return False
    for square_nr in range(9):
        if not valid_subset(get_square(grid,square_nr)):
            return False
    return True

def valid_subset(subset):
    for i in range(len(subset) - 1):
        if subset[i] == ".":
            continue
        for j in range(i + 1, len(subset)):
            if subset[i] == subset[j]:
                return False
    return True


def get_square(grid,nr):
    return grid[nr // 3][nr % 3 * 3:nr % 3 * 3 + 3] + grid[nr // 3 + 1][nr % 3 * 3:nr % 3 * 3 + 3] + grid[nr // 3 + 2][nr % 3 * 3:nr % 3 * 3 + 3]