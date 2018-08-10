class Solution(object):

    def isPalindrom(self, s):
        return s == s[::-1]

    def countSubstrings(self, s):
        count=0
        for length in range(1,len(s)+1):
            for position in range(len(s)-length+1):
                if self.isPalindrom(s[position:position+length]):
                    count += 1
        return count
