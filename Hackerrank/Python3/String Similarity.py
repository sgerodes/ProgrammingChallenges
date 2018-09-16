import os


def stringSimilarity(s):
    n = len(s)
    z = [None] * n
    z[0] = n
    L, R = 0, 0
    for i in range(1, n):
        if i > R:
            L = R = i
            while R < n and s[R - L] == s[R]:
                R += 1
            z[i] = R - L
            R -= 1
        else:
            k = i - L
            if z[k] < R - i + 1:
                z[i] = z[k]
            else:
                L = i
                while R < n and s[R - L] == s[R]:
                    R += 1
                z[i] = R - L
                R -= 1
    return sum(z)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = stringSimilarity(s)

        fptr.write(str(result) + '\n')

    fptr.close()
