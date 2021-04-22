import heapq
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = defaultdict(lambda:0)
        for i in nums:
            count[i] += 1
        limit = max(count)
        ans = [0] * (limit + 1)
        ans[0] = 0
        ans[1] = count[1] 
        for i in range(2,limit + 1):
            ans[i] = max(i * count[i] + ans[i - 2],ans[i - 1])
        return ans[limit]
