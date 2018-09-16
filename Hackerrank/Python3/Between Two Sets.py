import os


def getTotalX(a, b):
    cnt = 0
    minimum = max(a)
    maximum = min(b)
    candidates = range(minimum, maximum + 1, minimum)
    for num in candidates:
        passed = True
        for factor in b:
            if not factor % num == 0:
                passed = False
        for divider in a:
            if not num % divider == 0:
                passed = False
        if passed:
            cnt += 1
    return cnt


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
