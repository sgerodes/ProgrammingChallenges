class Solution:
    def reverseBits(self, n):
        return int("{0:b}".format(n).zfill(32)[::-1],2)