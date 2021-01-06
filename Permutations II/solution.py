import collections
import json
class Solution(object):
    def getval(self):
        return 0
    visited = None
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.visited = defaultdict(self.getval)
        self.dfs(nums)
        return map(lambda x:json.loads(x), self.visited.keys())
    def dfs(self, nums):
        self.visited[str(nums)] = 1
        for i in range(0,len(nums)):
            rest = nums[0:i] + nums[i + 1:]
            one = rest + [nums[i]]
            two = [nums[i]] + rest
            if self.visited[str(one)] == 0:
                self.dfs(one)
            if self.visited[str(two)] == 0:
                self.dfs(two)