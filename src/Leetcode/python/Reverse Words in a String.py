class Solution(object):
    def reverseWords(self, s):

        return " ".join([word for word in s.split()][::-1]).strip()