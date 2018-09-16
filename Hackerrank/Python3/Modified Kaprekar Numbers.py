def kaprekarNumbers(p, q):
    return " ".join([str(i) for i in range(p, q + 1) if is_kaprekar(i)]) or "INVALID RANGE"


def is_kaprekar(num):
    s = str(num ** 2)
    l = len(s) // 2
    return int(s[:l] or 0) + int(s[l:]) == num


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    answer = kaprekarNumbers(p, q)

    print(answer)
