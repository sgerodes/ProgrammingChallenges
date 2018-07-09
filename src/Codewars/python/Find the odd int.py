from collections import Counter
def find_it(seq):
    count=Counter(seq)
    for key in count.keys():
        if count[key]%2:
            return key