def solution(num):
    mapI=['','I','II','III','IV','V','VI','VII','VIII','IX']
    mapX=['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
    mapC=['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']

    return int(num/1000%10)*'M'+mapC[int(num/100%10)]+mapX[int(num/10%10)]+mapI[int(num%10)]
