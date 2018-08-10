class Solution(object):
    def numJewelsInStones(self, J, S):
        return sum(S.count(c) for c in J)