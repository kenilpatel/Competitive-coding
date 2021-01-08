import collections
class Solution(object):
    def getval(self):
        return 0
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: zint
        :rtype: int
        """
        max_cnt = 0
        sub = defaultdict(self.getval)
        for i in range(0,len(s)):
            for j in range(minSize, maxSize + 1):
                if i + j <= len(s):
                    string = s[i:i + j]
                    # print(string)
                    if len(set(string)) <= maxLetters and len(string) >= minSize and len(string) <= maxSize:
                        sub[string] = sub[string] + 1
                        if sub[string] > max_cnt:
                            max_cnt = sub[string]
        return max_cnt
