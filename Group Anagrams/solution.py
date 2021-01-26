class Solution(object):
    def get(self):
        return 0

    def getl(self):
        return []

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dword = defaultdict(self.getl)
        for w in strs:
            dword["".join(sorted(w))].append(w)
        return dword.values()
