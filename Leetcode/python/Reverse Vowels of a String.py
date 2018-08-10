class Solution:
    def reverseVowels(self, s):
        vowels="oeaiuOEAIU"
        rev_vowels_in_str=[c for c in s if c in vowels]
        ls=list(s)
        for i,c in enumerate(ls):
            if c in vowels:
                ls[i]=rev_vowels_in_str.pop()
        return "".join(ls)
