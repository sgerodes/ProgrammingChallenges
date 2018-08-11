class Solution:
    def countBits(self, num):
        return [bin(n).count('1') for n in range(num + 1)]
