class Solution:
    def isNumber(self, s):
        try:
            float(s)
        except Exception:
            return False
        return True
