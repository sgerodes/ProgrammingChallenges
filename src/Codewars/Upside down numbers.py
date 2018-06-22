from math import ceil
def solve(a, b):
    not_ud=['2','3','4','5','7']
    ud_map={'0':'0','1':'1','6':'9','8':'8','9':'6'}

    def is_up(number):
        snum=str(number)
        for i in range(ceil(len(snum)/2)):
            if snum[i] in not_ud or snum[-i-1] in not_ud:
                return False
            if not ud_map[snum[i]]==snum[-i-1]:
                return False
        return True

    count=0
    for i in range(a,b+1):
        if is_up(i):
            count+=1
    return count