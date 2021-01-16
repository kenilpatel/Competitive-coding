class Solution(object):
    def getval(self):
        return 0
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if len(s) < k:
            return False
        count = defaultdict(self.getval)
        for i in s:
            count[i] += 1
        odd = 0
        for key in count.keys():
            if count[key] % 2 != 0:
                odd += 1
        if odd > k:
            return False
        else:
            return True