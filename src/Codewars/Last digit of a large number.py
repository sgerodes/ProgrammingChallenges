def last_digit(n1, n2):
    if n2==0:
        return 1
    last_digit=n1%10
    if last_digit==0 or last_digit==1 or last_digit==5 or last_digit==6:
        return last_digit
    digit_map={2:[6,2,4,8],3:[1,3,9,7],4:[6,4],7:[1,7,9,3],8:[6,8,4,2],9:[1,9]}
    loop=digit_map[last_digit]
    return loop[n2%len(loop)]