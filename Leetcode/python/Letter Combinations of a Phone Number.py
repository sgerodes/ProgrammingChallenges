class Solution:
    def addLetter(self, rep, variant,digits):
        mapping={1:"",2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz",0:" "}
        if not digits:
            rep.append(variant)
            return 0
        for c in mapping[int(digits[0])]:
            Solution.addLetter(self,rep, variant+c,digits[1:])
        return 0

    def letterCombinations(self, digits):
        if digits == "" or "1" in digits or "0" in digits:
            return []
        rep=[]
        Solution.addLetter(self,rep,"",digits)

        return rep