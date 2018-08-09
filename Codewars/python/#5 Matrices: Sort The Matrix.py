def order(matrix):
    def transpose(array):
        return [list(column) for column in zip(*array)]

    for line in matrix:
        line.sort()

    matrix=transpose(matrix)

    for line in matrix:
        line.sort()

    return transpose(matrix)