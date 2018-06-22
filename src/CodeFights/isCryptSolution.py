def isCryptSolution(crypt, solution):
    mapping = {}
    for element in solution:
        mapping[element[0]] = element[1]
    for crypted_number in crypt:
        if len(crypted_number)>1 and mapping[crypted_number[0]] == '0':
            return False
    encrypt = list(map(lambda x2 : ''.join(list(map(lambda x : mapping[x], list(x2)))), crypt))
    print(encrypt[0],"+",encrypt[1],"==", encrypt[2])
    return eval(encrypt[0]) + eval(encrypt[1]) == eval(encrypt[2])