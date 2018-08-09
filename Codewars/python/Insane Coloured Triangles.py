from functools import lru_cache

@lru_cache(None)
def triangle(row):
    n = len(row) - 1
    result = 0
    for k, col in enumerate(row):
        temp = binomial_mod3(n, k) * color_to_num(col)
        result = (result + temp) % 3
    if n % 2 == 1:
        result = (- result) % 3
    return num_to_color(result)


def binomial_mod3(n, k):
    result = 1
    while n > 0:
        n3 = n % 3
        k3 = k % 3
        if k3 > n3:
            return 0
        temp = 1 if k3 == 0 or k3 == n3 else 2
        result = (result * temp) % 3
        n = n // 3
        k = k // 3
    return result


def color_to_num(col):
    return 0 if col == 'R' else 1 if col == 'G' else 2


def num_to_color(num):
    return 'R' if num == 0 else 'G' if num == 1 else 'B'