class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minl = [0]*len(nums)
        maxl = [0]*len(nums)
        minl[0] = nums[0]
        maxl[0] = nums[0]
        for i in range(1, len(nums)):
            minl[i] = min(nums[i], nums[i]*minl[i - 1], nums[i]*maxl[i - 1])
            maxl[i] = max(nums[i], nums[i]*minl[i - 1], nums[i]*maxl[i - 1])
        return max(maxl)
