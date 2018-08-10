import string

class Solution:
    def isPalindrome(self, s):
        if not s:
            return True
        alteredstr="".join([c for c in s if c in string.ascii_letters or c in string.digits ]).lower()
        for i in range(len(alteredstr)):
            #print("{} {} {}".format(i,alteredstr[i],alteredstr[-i-1]))
            if not alteredstr[i] == alteredstr[-i-1]:
                return False
        return True
