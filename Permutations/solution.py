class Solution(object):
    ans = None

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = set()
        self.dfs([], nums)
        return self.ans

    def dfs(self, alist, child):
        if child == []:
            self.ans.add(tuple(alist))
        if len(child) == 1:
            self.ans.add(tuple(alist + [child[0]]))
        for i in range(0, len(child)):
            new_child = child[0:i] + child[i + 1:]
            self.dfs(alist + [child[i]], new_child)
