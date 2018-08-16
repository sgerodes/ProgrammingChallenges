import sys


def plusMinus(arr):
    # Complete this function
    pos = 0
    neg = 0
    for num in arr:
        if num < 0:
            neg += 1
        elif num > 0:
            pos += 1
    print((0.0 + pos) / len(arr))
    print((0.0 + neg) / len(arr))
    print((len(arr) - pos - neg + 0.0) / len(arr))


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)
