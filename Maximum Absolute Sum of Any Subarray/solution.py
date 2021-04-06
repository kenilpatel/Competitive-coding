class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]
        maxi = pre[0]
        mini = pre[0]
        ans = 0
        for i in range(1,n + 1):
            if pre[i] >= 0:
                ans = max(ans,abs(pre[i] - mini))
            else:
                ans = max(ans,abs(pre[i] - maxi))
            maxi = max(maxi,pre[i])
            mini = min(mini,pre[i])
        return ans
