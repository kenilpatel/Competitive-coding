class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = {}
        right = {}
        count = 0
        for i in s:
            if i in right.keys():
                right[i] = right[i] + 1
            else:
                right[i] = 1
        for i in range(0, len(s)):
            if s[i] in left.keys():
                left[s[i]] = left[s[i]] + 1
            else:
                left[s[i]] = 1
            if s[i] in right.keys():
                right[s[i]] = right[s[i]] - 1
                if right[s[i]] == 0:
                    right.pop(s[i])
            if len(right.keys()) == len(left.keys()):
                count = count + 1
        return count
