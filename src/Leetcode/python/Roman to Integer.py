class Solution:
    def romanToInt(self, s):
        special_literals={'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        normal_literals={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num=0
        for n in ['IV','IX','XL','XC','CD','CM']:
            num+=s.count(n)*special_literals[n]
            s=s.replace(n, '')
        for n in ['I','V','X','L','C','D','M']:
            num+=s.count(n)*normal_literals[n]
        return num

