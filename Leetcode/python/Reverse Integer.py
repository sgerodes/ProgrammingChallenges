class Solution:
    def reverse(self, x):
        sign= -1 if x < 0 else 1
        rev= int(str(x*sign)[::-1])*sign
        return rev if rev in range(-(2**31),2**31-1) else 0
