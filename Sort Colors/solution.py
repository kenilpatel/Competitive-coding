class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        m = len(nums)
        for i in range(0, m):
            for j in range(i + 1, m):
                if nums[i] >= nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
