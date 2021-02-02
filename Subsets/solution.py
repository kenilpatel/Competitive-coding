class Solution(object):
    ans = None

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = []
        self.dfs([], nums)
        return self.ans

    def dfs(self, snow, childs):
        self.ans.append(snow)
        for i in range(0, len(childs)):
            item = childs[i]
            new_child = childs[i + 1:]
            self.dfs(snow + [item], new_child)
