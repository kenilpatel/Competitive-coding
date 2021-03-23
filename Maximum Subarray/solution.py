class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(1,n):
            nums[i] += nums[i - 1]
        minsum = 0
        maxsum = nums[0]
        for i in range(0,n):
            maxsum = max(maxsum,nums[i] - minsum)
            minsum = min(nums[i],minsum)
        return maxsum
