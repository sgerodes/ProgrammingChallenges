from collections import Counter
class Solution:
    def frequencySort(self, s):
        return ''.join([ c*freq for c,freq in Counter(s).most_common()])
