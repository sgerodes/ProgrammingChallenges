def sort_my_string(S):
    even = ''
    odd = ''
    for i in range(len(S)):
        if i % 2 == 0:
            even += S[i]
        else:
            odd += S[i]
    return even + " " + odd