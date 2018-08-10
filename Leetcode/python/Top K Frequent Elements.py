from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        return [ n for n,freq in Counter(nums).most_common(k)]