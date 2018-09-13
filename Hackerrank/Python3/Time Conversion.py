import os
def timeConversion(s):
    return s[:-2] if s[-2] == 'A' else str(int(s[:2]) + 12) + s[2:-2]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

