class Solution(object):
    def get(self):
        return 0

    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dict_c = defaultdict(self.get)
        low = 0
        high = 10
        ls = len(s)
        while high <= ls:
            dict_c[s[low:high]] += 1
            high += 1
            low += 1
        ans = []
        for key, val in dict_c.items():
            if val > 1:
                ans.append(key)
        return ans
