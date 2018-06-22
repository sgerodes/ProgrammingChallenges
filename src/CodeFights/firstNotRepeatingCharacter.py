def firstNotRepeatingCharacter(s):
    if len(s)==1:
        return s[0]
    for i in range(len(s)):
        for j in range(len(s)):
            if i == j:
                continue
            if s[i]==s[j]:
                break
            if j==len(s)-1:
                return s[i]
    return '_'