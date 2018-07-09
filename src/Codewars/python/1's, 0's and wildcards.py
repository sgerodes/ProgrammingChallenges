def possibilities(param):
    ans=[]
    variations = product(['0', '1'], repeat=param.count('?'))
    for variant in variations:
        ans.append(apply_variant(param, variant))
    #print(list(variations))
    return ans

def apply_variant(str, var):
    for num in var:
        str = str.replace('?', num, 1)
    return str