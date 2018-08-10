class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        smallest = min(strs, key=len)
        longest_prefix = ""

        for i,c in enumerate(smallest):
            ch=True
            for word in strs:
                if word[i]==c:
                    continue
                else:
                    ch=False
                    break
            if ch:
                longest_prefix+=c
            else:
                break

        return longest_prefix