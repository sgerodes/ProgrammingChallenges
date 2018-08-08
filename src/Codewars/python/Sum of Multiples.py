from math import ceil
def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return 'INVALID'
    return sum([i*n for i in range(1, ceil(m/n))])