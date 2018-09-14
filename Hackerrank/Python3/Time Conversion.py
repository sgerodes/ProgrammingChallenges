import os
def timeConversion(s):
    post_meridiem = s[-2] == 'P'
    _MM_SS = s[2:-2]
    HH = int(s[:2])
    if post_meridiem:
        if HH < 12:
            HH += 12
    else:
        if HH == 12:
            HH -= 12
    if HH < 10:
        HH = '0' + str(HH)
    else:
        HH = str(HH)
    return HH + _MM_SS


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

