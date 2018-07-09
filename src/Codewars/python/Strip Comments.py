def solution(string,markers):
    lst = string.split('\n')
    for sign in markers:
        for i in range(len(lst)):
            pos = lst[i].find(sign)
            if pos != -1:
                lst[i] = lst[i][:pos].strip()
    return '\n'.join(lst)