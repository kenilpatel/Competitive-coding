class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1 = sorted(s1)
        s2 = sorted(s2)
        if s1 < s2:
            n = len(s1)
            for i in range(n):
                if s1[i] <= s2[i]:
                    pass
                else:
                    return False
            return True
        else:
            n = len(s1)
            for i in range(n):
                if s2[i] <= s1[i]:
                    pass
                else:
                    return False
            return True
