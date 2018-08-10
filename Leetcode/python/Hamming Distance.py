class Solution:
    def hammingDistance(self, x, y):
        return len([i for i in format(x ^ y, 'b') if i=='1'])
