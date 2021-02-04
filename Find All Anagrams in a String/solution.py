class Solution(object):
    def get(self):
        return 0

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        qd = OrderedDict()
        wd = OrderedDict()
        # qd = defaultdict(self.get)
        # wd = defaultdict(self.get)
        lp = len(p)
        ls = len(s)
        if lp > ls:
            return []
        for key in "abcdefghijklmnopqrstuvwxyz":
            qd[key] = 0
            wd[key] = 0
        for i in p:
            qd[i] += 1
        low = 0
        high = lp - 1
        for i in range(0, high):
            wd[s[i]] += 1
        ans = []
        while high < ls:
            wd[s[high]] += 1
            if wd.items() == qd.items():
                ans.append(low)
            wd[s[low]] -= 1
            low += 1
            high += 1
        return ans
