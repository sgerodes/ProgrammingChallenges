class Solution:
    def titleToNumber(self, s):
        return sum([(ord(c.upper())-64)*26**position for position,c in enumerate(s[::-1])])
