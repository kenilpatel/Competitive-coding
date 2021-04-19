class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0 
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                break
            else:
                prev = s[i]
                i += 1
                j -= 1 
                while s[i] == prev and i + 1 < j:
                    i += 1
                while s[j] == prev and i < j - 1:
                    j -= 1   
        if s[i] == s[j] and i != j: 
            return 0
        return j - i + 1
